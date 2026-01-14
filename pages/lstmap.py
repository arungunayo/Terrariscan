
import ee
import geemap.foliumap as geemap
from streamlit_folium import st_folium

def load_view():
    import streamlit as st
    st.title("Land Surface Temperature (LST) Analysis")
    st.header("️ What is LST?")
    st.write("""
    Land Surface Temperature (LST) measures how hot the ground surface is, 
    derived from thermal infrared bands of satellites like Landsat-8/9.
    Unlike air temperature, LST directly reflects how surfaces such as 
    concrete, asphalt, and vegetation absorb and radiate heat.
    """)
    st.header("Overview of LST in Urban Heat Islands")
    st.write("""
    Urban Heat Islands (UHIs) form when built-up areas trap heat, raising LST compared to rural surroundings.
    - **High LST zones** → hotspots where vegetation is scarce.  
    - **Low LST zones** → cooler areas with trees, parks, or water bodies.  
    - **Correlation** → Higher NDVI (healthy vegetation) usually lowers LST.
    """)
    st.header("LST Map ")

    import streamlit as st
    import ee
    import geemap.foliumap as geemap
    from streamlit_folium import st_folium

    st.set_page_config(layout="wide")
    st.title("Land Surface Temperature (LST) – Ghaziabad")


    try:
        ee.Initialize(project='terrariscan')
    except Exception:
        ee.Authenticate()
        ee.Initialize(project='terrariscan')

    city = (
        ee.FeatureCollection("FAO/GAUL/2015/level2")
        .filter(ee.Filter.eq('ADM2_NAME', 'Ghaziabad'))
    )

    landsat_image = (
        ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
        .filterBounds(city)
        .filterDate('2024-01-01', '2024-12-31')
        .filter(ee.Filter.lt('CLOUD_COVER', 20))
        .median()
    )

    lst = (
        landsat_image.select('ST_B10')
        .multiply(0.00341802)
        .add(149.0)
        .subtract(273.15)
        .clip(city)
        .rename('LST')
    )

    lst_vis = {
        "min": 25,
        "max": 45,
        "palette": ["blue", "green", "yellow", "orange", "red"]
    }

    m = geemap.Map(center=[28.67, 77.45], zoom=10)
    m.addLayer(lst, lst_vis, "Land Surface Temperature (°C)")
    m.addLayer(city, {"color": "black"}, "City Boundary")
    m.add_colorbar(lst_vis, label="LST (°C)")

    st_folium(m, width=1200, height=700)
