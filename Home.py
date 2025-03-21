import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A ground water simulation framework, assessing the status of ground water resources under the influence of climate change in *Ouémé* river in Benin.
<https://groundwater-simulation-framework.com/>
"""

logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.sidebar.title("About")
st.sidebar.info(markdown)


# Customize page title
st.title("Ground Water Simulation Framework")

st.markdown(
    """
    The Upper Ouémé river catchment is located in northern Benin. It is one of the sub-catchments of the biggest river basin in Benin, the Ouémé river    
    """
)


# m2 = leafmap.Map()

# # Add a climate-related tile layer
# m2.add_tile_layer(
#     url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
#     name="ESRI Satellite",
#     attribution="ESRI"
# )

# # Add another tile layer for vegetation
# m2.add_tile_layer(
#     url="https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Terra_NDVI_8Day/default/2023-01-01/GoogleMapsCompatible_Level9/{z}/{y}/{x}.png",
#     name="MODIS NDVI",
#     attribution="NASA"
# )

# m2.to_streamlit(height=700)




row1_col1, row1_col2 = st.columns([2, 1.3])


    
with row1_col2:
    # Dropdown for selecting years
    options = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
    layers = st.multiselect("Select the year:", options, default=[])

    # Input precipitation variable (mm)
    precipitation = st.number_input(
        "Precipitation (mm)", min_value=0, max_value=200, value=100
    )

    # Input temperature variable (°C)
    temperature = st.number_input(
        "Temperature (°C)", min_value=0, max_value=50, value=25
    )

    # Input wind speed variable (m/s)
    wind_speed = st.number_input(
        "Wind Speed (m/s)", min_value=0, max_value=50, value=10
    )

with row1_col1:
    long = 9.412049
    lat = 2.300144
    m = folium.Map(location=[long, lat], zoom_start=8)  # Centered on Benin, Ouémé river long lat coordinates
    folium.TileLayer("OpenTopoMap").add_to(m)

    # Add a circle around the marker
    folium.Circle(
        location=[long, lat],
        radius=50000,  # Radius in meters
        color="green",
        fill=True,
        fill_color="blue"
    ).add_to(m)

    # folium.TileLayer("Stamen Watercolor").add_to(m)
    folium.TileLayer("OpenStreetMap").add_to(m)
    # folium.TileLayer("Stamen Terrain").add_to(m)

    folium.Marker(location=[long, lat], popup="Ouémé river").add_to(m)

    st_folium(m, width=700, height=500)

