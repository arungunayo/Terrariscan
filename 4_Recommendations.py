import streamlit as st
import pandas as pd

st.title("Recommendations")

st.header("Why Recommendations Matter")
st.write("""
After identifying priority zones, Terrascansi suggests practical greening strategies 
to reduce heat stress and improve urban resilience. These recommendations are tailored 
to each zone’s conditions and urgency.
""")

st.header("🌱 Recommended Strategies")
st.write("""
- **New Parks & Green Corridors** → Cool down high‑LST zones.  
- **Vegetation Buffers Along Roads** → Reduce heat and pollution exposure.  
- **Rooftop & Vertical Greening** → Add greenery in dense built‑up areas.  
- **Water Bodies & Reflective Surfaces** → Lower surface heat retention.  
- **Community‑Driven Planting Programs** → Engage citizens in sustainable action.
""")

st.header("Example Recommendation Matrix")

data = {
    "Zone": ["A", "B", "C", "D", "E"],
    "Priority_Index": [72.5, 65.3, 80.1, 50.2, 68.7],
    "Suggested_Action": [
        "New Park Development",
        "Vegetation Buffers",
        "Rooftop Greening",
        "Community Planting",
        "Water Body Restoration"
    ],
    "Expected_Impact": [
        "Reduce LST by 2‑3°C",
        "Lower roadside heat & AQI",
        "Cool dense urban blocks",
        "Increase vegetation cover",
        "Improve micro‑climate"
    ]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.success("These strategies help planners move from analysis to action, ensuring cooler, healthier, and more sustainable cities.")

#st.header("⚡ Why Terrascansi is Different at Recommendation Stage")

# #comparison = pd.DataFrame({
#    # "Traditional Tools": [
#       # "Stop at visualization",
#         "Leave action to external experts",
#         "No citizen engagement"
#     ],
#     "Terrascansi": [
#         "Suggests actionable greening strategies",
#         "Integrates analysis with decision support",
#         "Encourages community participation"
#     ]
# })

#st.table(comparison)
