import streamlit as st
import ee
import folium
from streamlit_folium import st_folium
import geemap.foliumap as geemap
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json

# ---------------------------------
# Streamlit config
# ---------------------------------
st.set_page_config(layout="wide")
st.title("Green Spaces Analysis – Ghaziabad")

# ---------------------------------
# Initialize Earth Engine
# ---------------------------------
ee.Initialize(project='My ')

# ---------------------------------
# City boundary
# ---------------------------------
city = (
    ee.FeatureCollection("FAO/GAUL/2015/level2")
    .filter(ee.Filter.eq("ADM2_NAME", "Ghaziabad"))
)

# ---------------------------------
# Sentinel-2 ImageCollection
# ---------------------------------
sentinel = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(city)
    .filterDate("2024-01-01", "2026-01-01")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))
    .median()
)

# ---------------------------------
# NDVI
# ---------------------------------
ndvi = sentinel.normalizedDifference(["B8", "B4"]).rename("NDVI")

# ---------------------------------
# NDVI threshold for green spaces
# ---------------------------------
green_spaces = ndvi.gt(0.3).selfMask()

# ---------------------------------
# Convert raster → vector polygons
# ---------------------------------
zones = green_spaces.reduceToVectors(
    geometry=city.geometry(),
    scale=10,
    geometryType="polygon",
    reducer=ee.Reducer.countEvery(),
    maxPixels=1e10
)

# ---------------------------------
# Add area + centroid
# ---------------------------------
def add_props(f):
    geom = f.geometry()
    centroid = geom.centroid(maxError=30)
    return f.set({
        "area_ha": geom.area(maxError=30).divide(10000),
        "centroid_lon": centroid.coordinates().get(0),
        "centroid_lat": centroid.coordinates().get(1)
    })

zones_with_props = zones.map(add_props)

# ---------------------------------
# Map
# ---------------------------------
m = folium.Map(location=[28.67, 77.42], zoom_start=10)

# NDVI layer
geemap.ee_tile_layer(
    ndvi,
    {"min": 0, "max": 1, "palette": ["white", "yellow", "green"]},
    "NDVI"
).add_to(m)

# Green spaces layer
geemap.ee_tile_layer(
    green_spaces,
    {"palette": ["006400"]},
    "Green Spaces"
).add_to(m)

# Boundary
geemap.ee_tile_layer(
    city.style(**{"color": "red", "fillColor": "00000000"}),
    {},
    "Ghaziabad Boundary"
).add_to(m)

folium.LayerControl().add_to(m)

# ---------------------------------
# Display map in Streamlit
# ---------------------------------
st_folium(m, width=1300, height=650)
