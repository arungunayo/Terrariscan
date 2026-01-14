import streamlit as st
from pathlib import Path
import pages.urban_heat_subpages.Overview
import pages.urban_heat_subpages.Vegetation_Correlation
import pages.lstmap
def load_view():
    print("uhi called")
    st.write("Rapid urbanization is shrinking green spaces and intensifying Urban Heat Islands. City planners often lack clear, data‑driven tools to identify high‑risk zones and act before crises escalate.Terrascansi transforms satellite imagery into actionable intelligence. It detects heat stress, tracks vegetation health, and ranks city zones by urgency. The system then suggests practical greening strategies — from new parks and corridors to rooftop vegetation — helping governments, NGOs, and communities build cooler, healthier, and more sustainable cities.")



    st.header("Empowering urban planners and citizens to combat heat inequality through data-driven insights.")
    st.subheader("Detect heat, measure vegetation, and prioritize greening interventions")
    st.write("Urban heat is not just a climate issue — it’s a social one. Across cities like Delhi, temperature disparities between neighborhoods are growing more severe, driven by unequal access to vegetation, poor infrastructure, and rapid urbanization. While some areas benefit from tree-lined streets and green parks, others endure blistering heat with little relief. These disparities aren’t random — they reflect deeper patterns of inequality. Terrascansi is a data-driven dashboard designed to expose and address this imbalance")
    if st.button("Explore Map",type="primary",width=250):
        st.info("Now open the sidebar and click **LST Map** to explore the interactive map.")


    st.write(
        """
        Our project is a satellite-driven green space intelligence system that goes beyond mapping existing vegetation to actively recommend where new green spaces should be created for maximum environmental impact. Using publicly available satellite imagery, we analyze vegetation patterns, urban land use, and historical change to identify areas with low green cover and high potential for improvement. The system then highlights priority zones for interventions such as parks, urban forests, and green buffers, providing planners, researchers, and communities with clear, data-backed insights to support sustainable and climate-resilient development.
        """
    )

    subtopic = st.selectbox("Explore More", [
        "Overview",
        "Vegetation Correlation"
    ])
    if subtopic == "Overview":
        pages.urban_heat_subpages.Overview.show_overview()
    elif subtopic == "Vegetation Correlation":
        pages.urban_heat_subpages.Vegetation_Correlation.show()
