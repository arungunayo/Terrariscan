import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

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

st.header(" Example Zone Data")

data = {
    "Zone": ["A", "B", "C", "D", "E"],
    "Avg_LST": [38, 36, 40, 33, 37],
    "NDVI": [0.25, 0.45, 0.20, 0.55, 0.30],
    "Historical_Loss": [0.15, 0.10, 0.20, 0.05, 0.18]
}
df = pd.DataFrame(data)

df["Priority_Index"] = df["Avg_LST"] * (1 - df["NDVI"]) + (df["Historical_Loss"] * 100)
df_sorted = df.sort_values("Priority_Index", ascending=False)

st.dataframe(df_sorted)
st.success("Zones with the highest Priority Index should be targeted first for greening interventions.")

st.header(" Priority Zones Map")

m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)

colors = ["red", "orange", "yellow", "green", "blue"]

for i, row in df_sorted.iterrows():
    folium.CircleMarker(
        location=[28.60 + i*0.02, 77.20 + i*0.01],
        radius=15,
        color=colors[i % len(colors)],
        fill=True,
        fill_opacity=0.6,
        popup=f"Zone {row['Zone']} | Priority Index: {row['Priority_Index']:.2f}"
    ).add_to(m)

st_folium(m, width=700, height=500)

# st.header("⚡ Why Terrascansi is Different at Zone Analysis Stage")
#
# comparison = pd.DataFrame({
#     "Traditional Tools": [
#         "Show raw maps only",
#         "No prioritization",
#         "Reactive after crisis"
#     ],
#     "Terrascansi": [
#         "Ranks zones by urgency",
#         "Provides actionable recommendations",
#         "Supports proactive planning"
#     ]
# })
#
# st.table(comparison)
