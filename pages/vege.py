import streamlit as st
import ee
import geemap.foliumap as geemap
from streamlit_folium import st_folium
def load_view():

    st.title(" Zone Analysis & Vegetation")

    st.header(" Why Zone Analysis?")
    st.write("""
    Terrascansi divides the urban area into grid-based zones.  
    Each zone is analyzed for:
    - **High LST (Land Surface Temperature)**  
    - **Low or declining NDVI (vegetation health)**  
    - **Historical vegetation loss**  
    
    This produces a **Priority Index** that ranks zones by urgency for greening interventions.
    """)

    # ---------- Streamlit setup ----------
    st.set_page_config(layout="wide")
    st.title("NDVI Map – Ghaziabad (Sentinel-2)")

    # ---------- Earth Engine init (SAFE) ----------
    try:
        ee.Initialize(project='terrariscan')
    except Exception:
        ee.Authenticate()
        ee.Initialize(project='terrariscan')

    # ---------- City boundary ----------
    city = (
        ee.FeatureCollection("FAO/GAUL/2015/level2")
        .filter(ee.Filter.eq('ADM2_NAME', 'Ghaziabad'))
    )

    # ---------- Sentinel-2 ----------
    sentinel = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(city)
        .filterDate('2024-01-01', '2024-12-31')
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
        .median()
    )

    # ---------- NDVI ----------
    ndvi = sentinel.normalizedDifference(['B8', 'B4']).rename('NDVI')

    # ---------- Visualization ----------
    ndvi_vis = {
        'min': 0,
        'max': 1,
        'palette': ['white', 'green']
    }

    # ---------- Map ----------
    m = geemap.Map(center=[28.67, 77.45], zoom=10)
    m.addLayer(ndvi, ndvi_vis, 'NDVI')
    m.addLayer(city, {'color': 'black'}, 'City Boundary')
    m.add_colorbar(ndvi_vis, label="NDVI")

    # ---------- Display ----------
    st_folium(m, width=1200, height=700)
