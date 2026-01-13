import streamlit as st
from pathlib import Path
st.title(":green[🌱Terrascansi — Urban Green Space Intelligence]")
st.write("Rapid urbanization is shrinking green spaces and intensifying Urban Heat Islands. City planners often lack clear, data‑driven tools to identify high‑risk zones and act before crises escalate.Terrascansi transforms satellite imagery into actionable intelligence. It detects heat stress, tracks vegetation health, and ranks city zones by urgency. The system then suggests practical greening strategies — from new parks and corridors to rooftop vegetation — helping governments, NGOs, and communities build cooler, healthier, and more sustainable cities.")
st.write("Written by Terrascansi team, 2025")
st.markdown(
    "<p style='font-family:Courier; color:blue; font-size:20px;'>",
    unsafe_allow_html=True
)


st.header("Empowering urban planners and citizens to combat heat inequality through data-driven insights.")
st.subheader("Detect heat, measure vegetation, and prioritize greening interventions")
st.write("Urban heat is not just a climate issue — it’s a social one. Across cities like Delhi, temperature disparities between neighborhoods are growing more severe, driven by unequal access to vegetation, poor infrastructure, and rapid urbanization. While some areas benefit from tree-lined streets and green parks, others endure blistering heat with little relief. These disparities aren’t random — they reflect deeper patterns of inequality. Terrascansi is a data-driven dashboard designed to expose and address this imbalance")
if st.button("Explore Map",type="primary",width=250):
    st.info("Now open the sidebar and click **LST Map** to explore the interactive map.")


APP_DIR = Path(__file__).parents[1]   # my_app
image_path = APP_DIR / "images" / "earth_on_fire.webp"

st.image(
    image_path,
    caption="Earth On Fire",
    width=400

)

st.write("Our mission is simple: to empower planners, researchers, and citizens with actionable insights into urban heat and vegetation coverage. Using satellite-derived data like Land Surface Temperature (LST) and NDVI (Normalized Difference Vegetation Index), EquiHeat visualizes where heat stress is highest and where green infrastructure is lacking. The platform is built to be intuitive, interactive, and scalable — whether you're analyzing one ward or an entire city.")
st.write("What sets EquiHeat apart is its focus on thermal justice — the idea that cooling resources should be distributed equitably. We don’t just show where it’s hot; we show why it’s hot, and what can be done about it. Our dashboard lets users upload their own CSV or GeoTIFF files, explore live maps, and receive ward-level recommendations for rooftop greening, tree planting, and policy interventions.")
st.write("This isn’t just a technical tool — it’s a storytelling engine. Investors and policymakers can use EquiHeat to identify high-risk zones, simulate cooling interventions, and prioritize funding where it’s needed most. The interface is designed for clarity and impact, with thematic color palettes, interactive layers, and per-page customization that makes each insight visually compelling.")
st.write("We believe that data should drive decisions — but only when it’s accessible. That’s why EquiHeat is built with open-source tools like Streamlit, Folium, and GeoPandas, making it affordable and adaptable for NGOs, municipalities, and academic researchers. The dashboard supports multiple formats, including CSV and GeoTIFF, and can be extended to include real-time sensor data, citizen feedback, or AI-based predictions.")
st.write("In a world facing rising temperatures and shrinking budgets, EquiHeat offers a pragmatic path forward. It’s not just about planting trees — it’s about planting them where they matter most. By combining geospatial analysis with equity-focused design, we aim to make cities cooler, fairer, and more resilient.")
st.write("Whether you're an investor looking to support climate innovation, a planner seeking data clarity, or a citizen advocating for your neighborhood, EquiHeat is your ally in the fight for thermal justice.")

subtopic = st.selectbox("Explore More", [
    "Overview",
    "Population Exposure",
    "Vegetation Correlation",
    "Priority Zones"
])
if subtopic == "Overview":
    st.subheader("Urban Heat Island Overview")
    st.write("Urban heat islands are areas, such as cities, that experience significantly higher temperatures than their surrounding rural areas. This phenomenon occurs due to several factors:Surface Absorption: Dark surfaces like asphalt and concrete absorb more sunlight and heat, leading to warmer temperatures. Reduced Ventilation: Tall buildings and narrow streets can block wind flow, preventing natural cooling. Human Activities: Energy consumption and industrial processes contribute to heat emissions, further increasing temperatures. Urban Geometry: The layout of cities can create urban canyons that trap heat. Overall, urban heat islands pose significant challenges to urban environments, affecting air quality and human health.")
elif subtopic == "Population Exposure":
    exec(open("urban_heat_subpages/Population_Exposure.py").read())
elif subtopic == "Vegetation Correlation":
    exec(open("urban_heat_subpages/Vegetation_Correlation.py").read())
elif subtopic == "Priority Zones":
    exec(open("urban_heat_subpages/Priority_Zones.py").read())
