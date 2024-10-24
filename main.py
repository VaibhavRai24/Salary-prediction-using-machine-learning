import streamlit as st
from app import show_predict_page
from explore_page import show_explore_page
page = st.sidebar.selectbox("Explore or Predicit", ("Predict", "Explore"))
if page=="Predict":
    show_predict_page()
else:
    show_explore_page()
