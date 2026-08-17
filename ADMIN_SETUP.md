# 🔧 Admin Setup Guide

AgriVision Pro requires **no login or credential upload from end users** —
satellite access, visitor tracking, and the contact form are all backed by
service credentials you (the admin) configure once. This guide covers that
one-time setup.

---

## 1. Google Earth Engine service account

Already configured in `.streamlit/secrets.toml` under `[gee_service_account]`.
The app initializes Earth Engine automatically on startup using these
credentials — visitors never see an authentication screen.

> ⚠️ **Known issue as of 2026-08-16**: the configured service account
> (`ee-aashishgautam533`) is currently missing the
> `roles/serviceusage.serviceUsageConsumer` role, which makes every Earth
> Engine call fail with *"Caller does not have required permission to use
> project..."*. Fix this at
> https://console.developers.google.com/iam-admin/iam?project=ee-aashishgautam533
> by granting that role (or an equivalent custom role with
> `serviceusage.services.use`) to the service account's `client_email`.
> Permission changes can take a few minutes to propagate.

---

## 2. Google Sheet for visitor count & contact form

The app persists the visitor counter and contact-form submissions to a
Google Sheet (Streamlit Cloud's filesystem is wiped on every redeploy/sleep,
so it can't hold this data itself).

1. Create a new Google Sheet (any name, e.g. "AgriVision Pro Data").
2. Share it with your service account's `client_email` (from
   `[gee_service_account]` in secrets.toml) as **Editor**.
3. Enable the **Google Sheets API** and **Google Drive API** for the same
   GCP project (console.cloud.google.com → APIs & Services → Library).
4. Copy the spreadsheet ID from its URL:
   `https://docs.google.com/spreadsheets/d/<THIS_PART>/edit`
5. Add it to `.streamlit/secrets.toml`:
   ```toml
   [sheets]
   spreadsheet_id = "your-spreadsheet-id"
   ```

The app creates two worksheets automatically the first time each is used:
- **Counter** — a single running total of all-time visits.
- **Contacts** — one row per contact-form submission (timestamp, name,
  email, organization, message).

If this isn't configured yet, the app degrades gracefully: the visitor count
just doesn't display, and the contact form shows a friendly "couldn't save"
message instead of erroring.

---

## 3. Weekly summary email (GitHub Actions)

`.github/workflows/weekly-summary.yml` runs every Monday at 13:00 UTC (and
can be triggered manually from the Actions tab) and emails a summary of
total visits and any new contact-form submissions from the past 7 days.

It runs `scripts/send_weekly_summary.py` outside of Streamlit, so it needs
its own copies of the credentials as **GitHub repo secrets** (Settings →
Secrets and variables → Actions):

| Secret | Value |
|---|---|
| `GEE_SERVICE_ACCOUNT_JSON` | The full service account JSON (same as `[gee_service_account]` in secrets.toml), as one line |
| `SHEET_ID` | Same spreadsheet ID as `[sheets].spreadsheet_id` above |
| `GMAIL_USER` | The Gmail address to send from |
| `GMAIL_APP_PASSWORD` | A Gmail **App Password** (not your login password) — generate one at https://myaccount.google.com/apppasswords (requires 2-Step Verification enabled) |
| `RECIPIENT_EMAIL` | Where the weekly summary should be sent, e.g. `aashish@cannabisforconservation.org` |

---

## 4. Keep the app awake (GitHub Actions)

`.github/workflows/keep-alive.yml` pings the live app every 15 minutes so
Streamlit Community Cloud doesn't put it to sleep from inactivity. It needs
no secrets — it just curls the public app URL
(`https://agrivision-pro.streamlit.app/`). If the app's URL ever changes,
update it in that workflow file.

---

## Summary of what runs where

| Concern | Mechanism |
|---|---|
| Satellite data access | Service account in secrets.toml — invisible to users |
| Visitor count / contact form | Google Sheet, read/written directly by the app |
| Weekly summary email | GitHub Actions cron → `scripts/send_weekly_summary.py` |
| App uptime | GitHub Actions cron pinging the live URL |
