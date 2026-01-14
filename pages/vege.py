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
    st.set_page_config(layout="wide")
    st.title("NDVI Map – Ghaziabad (Sentinel-2)")

    try:
        ee.Initialize(project='terrariscan')
    except Exception:
        ee.Authenticate()
        ee.Initialize(project='terrariscan')

    city = (
        ee.FeatureCollection("FAO/GAUL/2015/level2")
        .filter(ee.Filter.eq('ADM2_NAME', 'Ghaziabad'))
    )

    sentinel = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(city)
        .filterDate('2024-01-01', '2024-12-31')
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
        .median()
    )

    ndvi = sentinel.normalizedDifference(['B8', 'B4']).rename('NDVI')

    ndvi_vis = {
        'min': 0,
        'max': 1,
        'palette': ['white', 'green']
    }

    m = geemap.Map(center=[28.67, 77.45], zoom=10)
    m.addLayer(ndvi, ndvi_vis, 'NDVI')
    m.addLayer(city, {'color': 'black'}, 'City Boundary')
    m.add_colorbar(ndvi_vis, label="NDVI")


    st_folium(m, width=1200, height=700)
