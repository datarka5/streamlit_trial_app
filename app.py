import streamlit as st
from streamlit_profiler import Profiler


# from streamlit_option_menu import option_menu
st.set_page_config(page_title="Streamlit cloud testing", layout="wide", page_icon="chart_with_upwards_trend")

st.title("Streamlit cloud testing")

tab_about, tab_tutorial = st.tabs(["About", "Tutorials"])
