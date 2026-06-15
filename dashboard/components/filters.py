import streamlit as st

def sidebar_filters(df):

    st.sidebar.header("Filters")

    selected_year = st.sidebar.selectbox(
        "Select Year",
        sorted(df["year"].dropna().unique())
    )

    selected_vehicle = st.sidebar.selectbox(
        "Vehicle Type",
        sorted(df["vehicle_type"].dropna().unique())
    )

    return selected_year, selected_vehicle