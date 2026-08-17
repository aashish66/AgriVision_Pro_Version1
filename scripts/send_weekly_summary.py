"""
AgriVision Pro V3 - Weekly Summary Email
==========================================
Standalone script run on a schedule by GitHub Actions
(.github/workflows/weekly-summary.yml). Reads the visitor count and recent
contact-form submissions from the same Google Sheet the app writes to, and
emails a summary via Gmail SMTP.

Not part of the Streamlit app - credentials come from environment variables
(GitHub Actions secrets), not st.secrets.

Required environment variables:
    GEE_SERVICE_ACCOUNT_JSON  - full service account JSON, as one line
    SHEET_ID                  - the Google Sheet's spreadsheet ID
    GMAIL_USER                - Gmail address to send from
    GMAIL_APP_PASSWORD        - Gmail app password (not the account password)
    RECIPIENT_EMAIL           - who receives the weekly summary
"""

import json
import os
import smtplib
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText

import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def get_spreadsheet():
    creds_info = json.loads(os.environ["GEE_SERVICE_ACCOUNT_JSON"])
    credentials = Credentials.from_service_account_info(creds_info, scopes=SCOPES)
    client = gspread.authorize(credentials)
    return client.open_by_key(os.environ["SHEET_ID"])


def build_summary(spreadsheet) -> str:
    counter_values = spreadsheet.worksheet("Counter").get_all_values()
    total_visits = counter_values[1][0] if len(counter_values) > 1 else "0"

    contact_rows = spreadsheet.worksheet("Contacts").get_all_values()[1:]  # skip header

    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    recent = []
    for row in contact_rows:
        try:
            timestamp = datetime.fromisoformat(row[0])
        except (ValueError, IndexError):
            continue
        if timestamp >= cutoff:
            recent.append(row)

    lines = [
        "AgriVision Pro - Weekly Summary",
        "=" * 32,
        f"Total visits (all-time): {total_visits}",
        f"New contact-form submissions (last 7 days): {len(recent)}",
        "",
    ]
    for row in recent:
        timestamp, name, email, organization, message = (row + [""] * 5)[:5]
        lines.append(f"- {timestamp} | {name} <{email}> | {organization}")
        if message:
            lines.append(f'  "{message}"')
    if not recent:
        lines.append("(no new submissions this week)")

    return "\n".join(lines)


def send_email(body: str):
    message = MIMEText(body)
    message["Subject"] = "AgriVision Pro - Weekly Summary"
    message["From"] = os.environ["GMAIL_USER"]
    message["To"] = os.environ["RECIPIENT_EMAIL"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["GMAIL_USER"], os.environ["GMAIL_APP_PASSWORD"])
        server.send_message(message)


def main():
    spreadsheet = get_spreadsheet()
    summary = build_summary(spreadsheet)
    send_email(summary)
    print(summary)


if __name__ == "__main__":
    main()
