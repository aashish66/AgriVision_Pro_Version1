"""
AgriVision Pro V3 - Earth Engine Initialization
=================================================
Connects to Google Earth Engine using the service account configured in
.streamlit/secrets.toml, so the app requires no end-user login or
credential upload. Falls back to a locally-authenticated
`earthengine authenticate` session for local development.
"""

import streamlit as st
import ee


@st.cache_resource(show_spinner=False)
def _initialize_earth_engine() -> bool:
    """Initialize Earth Engine once per app process. Returns True if ready."""
    try:
        if hasattr(st, 'secrets') and 'gee_service_account' in st.secrets:
            import google.oauth2.service_account

            creds_data = dict(st.secrets['gee_service_account'])
            credentials = google.oauth2.service_account.Credentials.from_service_account_info(
                creds_data,
                scopes=['https://www.googleapis.com/auth/earthengine']
            )
            ee.Initialize(
                credentials,
                project=creds_data.get('project_id'),
                opt_url='https://earthengine-highvolume.googleapis.com'
            )
            ee.Number(1).getInfo()
            return True
    except Exception:
        pass

    # Local development fallback: credentials from `earthengine authenticate`
    try:
        ee.Initialize()
        ee.Number(1).getInfo()
        return True
    except Exception:
        return False


def ensure_ee_initialized() -> bool:
    """Return True if Earth Engine is ready to use."""
    return _initialize_earth_engine()
