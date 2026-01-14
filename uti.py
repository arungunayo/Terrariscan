import streamlit as st
import base64
from streamlit.components.v1 import html

from paths import NAVBAR_PATHS


def inject_custom_css():
    """Inject global CSS for the navbar and layout."""
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def get_current_route():
    """
    Read the current route from the URL query params.

    Supports both the modern `st.query_params` API and the older
    `st.experimental_get_query_params` so navigation works across
    Streamlit versions.
    """
    try:
        # Newer Streamlit versions
        params = getattr(st, "query_params", None)
        if params is None:
            # Fallback for older versions
            params = st.experimental_get_query_params()

        nav = params.get("nav")
        if isinstance(nav, list):
            return nav[0] if nav else None
        return nav
    except Exception:
        return None


def navbar_component():
    """
    Render a horizontal navbar in the main page DOM.

    The links update the app URL (e.g. `/?nav=uhi`) so that
    `get_current_route()` can route to the correct view.
    """
    navbar_items = ""
    for label, route in NAVBAR_PATHS.items():
        navbar_items += f'<a class="navitem" href="/?nav={route}">{label}</a>'

    navbar_html = f"""
    <div class="navbar">
        {navbar_items}
    </div>
    """

    st.markdown(navbar_html, unsafe_allow_html=True)
