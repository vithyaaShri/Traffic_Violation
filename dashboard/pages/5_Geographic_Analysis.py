import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

USERNAME = "root"
PASSWORD = "root"
DATABASE = "traffic_violation_db"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)

st.title("🌍 Geographic Analysis")

# Top Driver Cities

st.subheader("Top Driver Cities")

city_df = pd.read_sql(
    """
    SELECT driver_city,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY driver_city
    ORDER BY total DESC
    LIMIT 15
    """,
    engine
)

fig1 = px.bar(
    city_df,
    x="driver_city",
    y="total",
    title="Top Driver Cities"
)

st.plotly_chart(fig1, use_container_width=True)

# Driver States

st.subheader("Driver States")

state_df = pd.read_sql(
    """
    SELECT driver_state,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY driver_state
    ORDER BY total DESC
    LIMIT 15
    """,
    engine
)

fig2 = px.bar(
    state_df,
    x="driver_state",
    y="total",
    title="Top Driver States"
)

st.plotly_chart(fig2, use_container_width=True)

# Latitude / Longitude Map

st.subheader("Traffic Violations Map")

map_df = pd.read_sql(
    """
    SELECT latitude,
           longitude
    FROM traffic_violations
    WHERE latitude IS NOT NULL
      AND longitude IS NOT NULL
    LIMIT 5000
    """,
    engine
)

st.map(map_df)