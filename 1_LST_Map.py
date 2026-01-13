import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
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
st.header("LST Map Preview")
m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)
folium.CircleMarker(
    location=[28.61, 77.23],
    radius=20,
    color="red",
    fill=True,
    fill_opacity=0.6,
    popup="High LST Zone"
).add_to(m)
folium.CircleMarker(
    location=[28.65, 77.18],
    radius=20,
    color="green",
    fill=True,
    fill_opacity=0.6,
    popup="Low LST Zone"
).add_to(m)
st_folium(m, width=700, height=500)
st.info("Later, replace these demo markers with Landsat thermal raster layers processed via Google Earth Engine.")
st.header("How LST Helps in UHI Analysis")
st.write("""
- **Pinpoints hotspots**: Identifies areas where heat stress is highest.  
- **Guides greening**: Shows where vegetation buffers or parks are most needed.  
- **Supports health & policy**: Helps planners reduce heat exposure for vulnerable populations.
""")
# st.header("⚡ Why Terrascansi is Different")
# comparison = pd.DataFrame({
#     "Old Heavy Tools": [
#         "Show vegetation only",
#         "Static maps",
#         "Analyst-centric",
#         "Retrospective (past data only)",
#         "Heavy, complex platforms"
#     ],
#     "Terrascansi": [
#         "Suggest new vegetation strategies",
#         "Interactive decision-support",
#         "Accessible to planners, NGOs, communities",
#         "Forward-looking (predictive + recommendations)",
#         "Lightweight, Streamlit-based, easy to use"
#     ]
# })
# st.table(comparison)
