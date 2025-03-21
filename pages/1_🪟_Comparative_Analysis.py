import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A ground water simulation framework, assessing the status of ground water resources under the influence of climate change in *Ouémé* river in Benin.
<https://groundwater-simulation-framework.com/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Current state VS projected ground water resources")
col1, col2 = st.columns([4, 1])

# Define available layers as dictionaries
available_layers = {
    "ESA WorldCover 2020 S2 FCC": "ESA WorldCover 2020 S2 FCC",
    "ESA WorldCover 2020": "ESA WorldCover 2020",
    "OpenStreetMap": "OpenStreetMap",
    "OpenTopoMap": "OpenTopoMap",
}

# Allow users to select layers for the left and right maps
with col2:
    left_layer_title = st.selectbox("Select left layer:", list(available_layers.keys()))
    right_layer_title = st.selectbox("Select right layer:", list(available_layers.keys()))

# Get the actual layer names from the dictionary
left_layer = available_layers[left_layer_title]
right_layer = available_layers[right_layer_title]

with col1:
    # Initialize the map
    m = leafmap.Map()
    m.split_map(left_layer=left_layer, right_layer=right_layer)
    m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

    # Render the map in Streamlit
    m.to_streamlit(height=700)