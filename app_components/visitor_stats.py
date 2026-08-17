"""
AgriVision Pro V3 - Visitor Stats Component
============================================
Persistent visitor counter backed by Google Sheets (see sheets_utils.py).
Counts once per session and displays the all-time total. If Sheets isn't
configured yet, fails silently rather than breaking the page.
"""

from datetime import datetime
from typing import Optional

import streamlit as st

from app_components.sheets_utils import increment_visitor_count, get_visitor_count


class VisitorStatsComponent:
    """Persistent visitor counter component."""

    def __init__(self):
        if 'visitor_counted' not in st.session_state:
            st.session_state.visitor_counted = False

    def _current_count(self) -> Optional[int]:
        try:
            if not st.session_state.visitor_counted:
                st.session_state.visitor_counted = True
                return increment_visitor_count()
            return get_visitor_count()
        except Exception:
            return None

    def render_footer(self):
        """Render visitor stats in footer."""
        count = self._current_count()

        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            if count is not None:
                st.caption(f"👥 Total visitors: {count}")
        with col2:
            st.caption(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        with col3:
            st.caption("🌾 AgriVision Pro V3")
