import streamlit as st
import base64
from streamlit.components.v1 import html

from paths import NAVBAR_PATHS


def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.query_params['nav']
    except:
        return None


def navbar_component():
    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += f'<a class="navitem" href="/?nav={value}">{key}</a>'

    navbar_html = f"""
    <div class="navbar">
        {navbar_items}
    </div>

    <script>
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        for (var i = 0; i < navigationTabs.length; i++) {{
            navigationTabs[i].removeAttribute('target');
        }}
    </script>
    """

    html(navbar_html, height=80)
