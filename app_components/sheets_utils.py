"""
AgriVision Pro V3 - Persistent Stats & Contact Storage
========================================================
Backs the visitor counter and the landing-page contact form with a Google
Sheet, using the same service account configured for Earth Engine. Streamlit
Cloud's filesystem is ephemeral, so this is the persistence layer instead of
local files.

Requires in .streamlit/secrets.toml:
    [sheets]
    spreadsheet_id = "..."

And the target Sheet shared (Editor access) with the service account's
client_email from [gee_service_account].
"""

from datetime import datetime, timezone

import streamlit as st

SHEETS_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

COUNTER_SHEET = "Counter"
CONTACTS_SHEET = "Contacts"


def _get_spreadsheet():
    import gspread
    import google.oauth2.service_account

    creds_data = dict(st.secrets['gee_service_account'])
    credentials = google.oauth2.service_account.Credentials.from_service_account_info(
        creds_data, scopes=SHEETS_SCOPES
    )
    client = gspread.authorize(credentials)
    return client.open_by_key(st.secrets['sheets']['spreadsheet_id'])


def _get_or_create_worksheet(spreadsheet, name: str, header: list):
    try:
        return spreadsheet.worksheet(name)
    except Exception:
        worksheet = spreadsheet.add_worksheet(title=name, rows=1000, cols=len(header))
        worksheet.append_row(header)
        return worksheet


def increment_visitor_count() -> int:
    """Increment the persistent visitor counter by 1 and return the new total."""
    spreadsheet = _get_spreadsheet()
    worksheet = _get_or_create_worksheet(spreadsheet, COUNTER_SHEET, ["total_visits"])
    values = worksheet.get_all_values()
    if len(values) < 2:
        worksheet.append_row(["1"])
        return 1
    count = int(values[1][0]) + 1
    worksheet.update_cell(2, 1, count)
    return count


@st.cache_data(ttl=60, show_spinner=False)
def get_visitor_count() -> int:
    """Read the current persistent visitor count (cached briefly to limit API calls)."""
    spreadsheet = _get_spreadsheet()
    worksheet = _get_or_create_worksheet(spreadsheet, COUNTER_SHEET, ["total_visits"])
    values = worksheet.get_all_values()
    if len(values) < 2:
        return 0
    return int(values[1][0])


def log_contact_submission(name: str, email: str, organization: str, message: str) -> None:
    """Append a landing-page contact-form submission as a new row."""
    spreadsheet = _get_spreadsheet()
    worksheet = _get_or_create_worksheet(
        spreadsheet, CONTACTS_SHEET,
        ["timestamp", "full_name", "email", "organization", "message"]
    )
    worksheet.append_row([
        datetime.now(timezone.utc).isoformat(timespec="seconds"),
        name, email, organization, message
    ])
