import streamlit as st
import uti as utl
import pages.uhi as uhi
import pages.vege as vege
import pages.dup as dup
import pages.lstmap as lstmap

st.set_page_config(layout="wide", page_title='Navbar sample')
st.title(":green[🌱Terrascansi — Urban Green Space Intelligence]")
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()

    if route is None or route == "uhi":
        uhi.load_view()

    elif route == "dup":
        dup.load_view()

    elif route == "lstmap":
        lstmap.load_view()

    elif route == "vege":
        vege.load_view()
navigation()