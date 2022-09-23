import streamlit as st
from streamlit_profiler import Profiler


# from streamlit_option_menu import option_menu
st.set_page_config(page_title="Global Sales Block", layout="wide", page_icon="chart_with_upwards_trend")

st.title("Global Sales Block")
# https://brocoders.com/blog/mapbox-vs-google-maps-vs-openstreetmap/#:~:text=With%20Google%20Maps%20and%20Mapbox,all%20the%20bells%20and%20whistles.

tab_about, tab_tutorial = st.tabs(["About", "Tutorials"])
