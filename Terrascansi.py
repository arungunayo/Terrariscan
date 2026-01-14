# ============================================================
# Terrascansi — Urban Green Space Intelligence Dashboard
# ------------------------------------------------------------
# INTENT:
# This file is meant to be a Streamlit web application that:
# - Visualizes Urban Heat Islands (UHI)
# - Shows Land Surface Temperature (LST)
# - Analyzes vegetation using NDVI
# - Ranks urban zones by greening priority
# - Provides actionable recommendations
#
# Navigation is handled manually using st.session_state.page
# Folium is used for maps, Streamlit for UI
#
# NOTE:
# This file contains MANY ERRORS and DUPLICATIONS.
# Errors are MARKED, NOT FIXED.
# ============================================================

import streamlit as st
from pathlib import Path
import folium
from streamlit_folium import st_folium
import pandas as pd

# ------------------------------------------------------------
# Streamlit page configuration
# ------------------------------------------------------------
# ❌ ERROR: st.set_page_config() is called MULTIPLE TIMES
# Streamlit allows this ONLY ONCE per app
st.set_page_config(page_title="Terrascansi", layout="wide")

# ------------------------------------------------------------
# Custom CSS + Branding Header
# ------------------------------------------------------------
# INTENT:
# Add custom styles and create a visually appealing title
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #2E8B57;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            margin-bottom: 30px;
            color: #444;
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }
        .nav-buttons a {
            background-color: #e6f2ec;
            color: #2E8B57;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            font-size: 16px;
        }
        .nav-buttons a:hover {
            background-color: #cce5d6;
        }
        </style>
        <div class='title'>🌱Terrascansi — Urban Green Space Intelligence</div>
        <div class='subtitle'>
            Empowering urban planners and citizens to combat heat inequality
            through data-driven insights
        </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Session State Navigation Setup
# ------------------------------------------------------------
# INTENT:
# Acts like a router for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Urban Heat Island"

# ------------------------------------------------------------
# Navbar button styling
# ------------------------------------------------------------
st.markdown("""
    <style>
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }
        .nav-buttons button {
            background-color: #e6f2ec;
            color: #2E8B57;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            font-size: 16px;
            border: none;
        }
        .nav-buttons button:hover {
            background-color: #cce5d6;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# App title (duplicated branding)
# ------------------------------------------------------------
st.markdown("<h1 style='text-align:center;'>🌱 Terrascansi — Urban Green Space Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Empowering urban planners and citizens to combat heat inequality through data-driven insights</h4>", unsafe_allow_html=True)

# ------------------------------------------------------------
# Navigation buttons (manual page switcher)
# ------------------------------------------------------------
# INTENT:
# Clicking a button updates st.session_state.page
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Urban Heat Island"):
        st.session_state.page = "Urban Heat Island"

with col2:
    if st.button("LST Map"):
        st.session_state.page = "LST Map"

with col3:
    if st.button("Data Upload"):
        st.session_state.page = "Data Upload"

with col4:
    if st.button("Vegetation"):
        st.session_state.page = "Vegetation"

with col5:
    if st.button("Recommendations"):
        st.session_state.page = "Recommendations"

# ============================================================
# PAGE: URBAN HEAT ISLAND
# ============================================================
if st.session_state.page == "Urban Heat Island":

    # INTENT:
    # Landing page + storytelling + motivation
    st.subheader("Detect heat, measure vegetation, and prioritize greening interventions")

    st.write("""
        Urban heat is not just a climate issue — it’s a social one.
        This section frames UHI as a problem of inequality and access to green spaces.
    """)

    # ❌ ERROR: st.button does NOT support "width" argument
    if st.button("Explore Map", type="primary", width=250):
        st.info("Navigate to LST Map page")

    # INTENT:
    # Load local image for emotional storytelling
    APP_DIR = Path(__file__).parent
    image_path = APP_DIR / "images" / "earth_on_fire.webp"

    # ❌ ERROR POSSIBILITY: Image path may not exist
    st.image(image_path, caption="Earth On Fire", width=400)

    # INTENT:
    # Mission & platform explanation (pitch-heavy)
    st.write("Mission, equity focus, open-source philosophy, scalability")

    # --------------------------------------------------------
    # Sub-navigation inside Urban Heat Island
    # --------------------------------------------------------
    subtopic = st.selectbox("Explore More", [
        "Overview",
        "Population Exposure",
        "Vegetation Correlation",
        "Priority Zones"
    ])

    if subtopic == "Overview":
        st.subheader("Urban Heat Island Overview")
        st.write("Educational explanation of UHI")

    elif subtopic == "Population Exposure":
        # ❌ MAJOR RED FLAG:
        # exec() dynamically runs another Python file
        # INTENT: modular subpages
        exec(open("urban_heat_subpages/Population_Exposure.py").read())

    elif subtopic == "Vegetation Correlation":
        exec(open("urban_heat_subpages/Vegetation_Correlation.py").read())

    elif subtopic == "Priority Zones":
        exec(open("urban_heat_subpages/Priority_Zones.py").read())

# ============================================================
# PAGE: LST MAP
# ============================================================
elif st.session_state.page == "LST Map":

    # INTENT:
    # Educational + demo visualization of Land Surface Temperature
    st.title("Land Surface Temperature (LST) Analysis")

    st.write("""
        Explains what LST is and why it matters for Urban Heat Islands.
    """)

    # INTENT:
    # Demo map centered on Delhi
    m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)

    # INTENT:
    # Fake markers to demonstrate hot vs cool zones
    folium.CircleMarker(
        location=[28.61, 77.23],
        radius=20,
        color="red",
        fill=True,
        popup="High LST Zone"
    ).add_to(m)

    folium.CircleMarker(
        location=[28.65, 77.18],
        radius=20,
        color="green",
        fill=True,
        popup="Low LST Zone"
    ).add_to(m)

    st_folium(m, width=700, height=500)

# ============================================================
# PAGE: DATA UPLOAD
# ============================================================
elif st.session_state.page == "Data Upload":

    # INTENT:
    # Allow users to upload their own satellite/tabular data
    st.title("Data Upload & Feature Extraction")

    uploaded_file = st.file_uploader(
        "Upload satellite data (CSV or GeoTIFF)",
        type=["csv", "tif", "tiff"]
    )

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # INTENT:
        # CSV preview
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())

        # INTENT:
        # Placeholder for raster processing
        else:
            st.write("GeoTIFF uploaded. Raster processing planned.")

    # INTENT:
    # Example NDVI trend (fake data)
    data = {
        "Date": ["2020", "2021", "2022", "2023", "2024"],
        "NDVI": [0.45, 0.42, 0.40, 0.38, 0.35]
    }

    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Date"))

# ============================================================
# PAGE: VEGETATION / ZONE ANALYSIS
# ============================================================
elif st.session_state.page == "Vegetation":

    # INTENT:
    # Rank urban zones by urgency for greening
    st.title("Zone Analysis & Vegetation")

    data = {
        "Zone": ["A", "B", "C", "D", "E"],
        "Avg_LST": [38, 36, 40, 33, 37],
        "NDVI": [0.25, 0.45, 0.20, 0.55, 0.30],
        "Historical_Loss": [0.15, 0.10, 0.20, 0.05, 0.18]
    }

    df = pd.DataFrame(data)

    # INTENT:
    # Priority Index = Heat + Vegetation loss + history
    df["Priority_Index"] = (
        df["Avg_LST"] * (1 - df["NDVI"])
        + (df["Historical_Loss"] * 100)
    )

    df_sorted = df.sort_values("Priority_Index", ascending=False)
    st.dataframe(df_sorted)

# ============================================================
# PAGE: RECOMMENDATIONS
# ============================================================
elif st.session_state.page == "Recommendations":

    # INTENT:
    # Convert analysis into actionable policy suggestions
    st.title("Recommendations")

    data = {
        "Zone": ["A", "B", "C", "D", "E"],
        "Priority_Index": [72.5, 65.3, 80.1, 50.2, 68.7],
        "Suggested_Action": [
            "New Park Development",
            "Vegetation Buffers",
            "Rooftop Greening",
            "Community Planting",
            "Water Body Restoration"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# ============================================================
# Sidebar hiding (full-screen experience)
# ============================================================
st.markdown("""
   <style>
   [data-testid="stSidebar"] { display: none; }
   [data-testid="stSidebarNav"] { display: none; }
   </style>
""", unsafe_allow_html=True)

# ============================================================
# ❌ CRITICAL ISSUE:
# EVERYTHING ABOVE IS DUPLICATED AGAIN IN YOUR FILE
# INTENT: accidental copy-paste or bad merge
# ============================================================
