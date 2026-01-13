import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
st.markdown(
    """
    <style>
    .stApp { background-color: #FFF8F0; }
    </style>
    """,
    unsafe_allow_html=True
)
st.title(" Data Upload & Feature Extraction")
st.header("🌐 Data Sources")
st.write("""
Terrascansi uses open satellite data to monitor vegetation and heat stress:

- **Sentinel‑2 imagery** → High‑resolution vegetation data for NDVI.  
- **Landsat‑8/9 thermal bands** → Land Surface Temperature (LST).  
- **Multi‑temporal datasets** → Seasonal and historical trend analysis.
""")
st.info("These sources are free, global, and updated regularly — making Terrascansi scalable and future‑ready.")
st.header("Upload Your Own Data")
uploaded_file = st.file_uploader("Upload satellite data (CSV or GeoTIFF)", type=["csv", "tif", "tiff"])
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(df.head())
    else:
        st.write("GeoTIFF uploaded. Raster visualization will be processed in future integration.")
st.header("🔍 Feature Extraction")
st.write("""
From raw satellite data, Terrascansi extracts key indicators:
- **NDVI (Normalized Difference Vegetation Index)** → Vegetation density and health.  
- **LST (Land Surface Temperature)** → Detects Urban Heat Islands.  
- **Change Detection** → Highlights vegetation degradation over time.
""")
data = {
    "Date": ["2020", "2021", "2022", "2023", "2024"],
    "NDVI": [0.45, 0.42, 0.40, 0.38, 0.35]
}
df = pd.DataFrame(data)
st.subheader(" NDVI Trend Example")
st.line_chart(df.set_index("Date"))
st.header("Sample Map Preview")
m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)  # Example: Delhi coords
folium.CircleMarker(
    location=[28.61, 77.23],
    radius=15,
    color="green",
    fill=True,
    fill_opacity=0.6,
    popup="High NDVI (Healthy Vegetation)"
).add_to(m)
folium.CircleMarker(
    location=[28.65, 77.18],
    radius=15,
    color="red",
    fill=True,
    fill_opacity=0.6,
    popup="Low NDVI (Vegetation Loss)"
).add_to(m)
st_folium(m, width=700, height=500)
# st.header("⚡ Why Terrascansi is Different at This Stage")
# comparison = pd.DataFrame({
#     "Traditional Tools": [
#         "Require manual preprocessing",
#         "Static vegetation maps",
#         "Limited temporal analysis"
#     ],
#     "Terrascansi": [
#         "Automated NDVI & LST extraction",
#         "Interactive maps with overlays",
#         "Multi‑year trend detection"
#     ]
# })
# st.table(comparison)
