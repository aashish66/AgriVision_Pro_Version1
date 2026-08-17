"""
AgriVision Pro V3 - Contact Form Component
=============================================
Optional "tell us about yourself" form shown on the landing page. Never
blocks access to the tools - it just logs interested visitors to Google
Sheets (see sheets_utils.py) for a weekly summary email.
"""

import streamlit as st

from app_components.sheets_utils import log_contact_submission


class ContactFormComponent:
    """Optional visitor contact form."""

    def render(self):
        if st.session_state.get('contact_submitted'):
            st.success("✅ Thanks for reaching out — we'll be in touch!")
            return

        with st.expander("👋 Tell us a bit about yourself (optional)"):
            with st.form("contact_form", clear_on_submit=True):
                name = st.text_input("Full Name", placeholder="Your name")
                email = st.text_input("Email Address", placeholder="your.email@example.com")
                organization = st.text_input("Address / Organization", placeholder="Your organization or address")
                message = st.text_area("Message", placeholder="Write your message here...", height=120)
                submitted = st.form_submit_button("Submit", type="primary")

            if submitted:
                if not name or not email:
                    st.warning("Please provide at least your name and email.")
                else:
                    try:
                        log_contact_submission(name, email, organization, message)
                        st.session_state.contact_submitted = True
                        st.rerun()
                    except Exception:
                        st.warning("⚠️ Couldn't save your info right now — please try again later.")
