import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
# from utils.database_connection import get_engine
import plotly.express as px

USERNAME = "root"
PASSWORD = "root"
DATABASE = "traffic_violation_db"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)
# engine = get_engine()
st.title("🚗 Vehicle Analysis")

# ---------------------------------------
# Top Vehicle Makes
# ---------------------------------------

vehicle_df = pd.read_sql(
    """
    SELECT make,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY make
    ORDER BY total DESC
    LIMIT 10
    """,
    engine
)

fig1 = px.bar(
    vehicle_df,
    x="make",
    y="total",
    title="Top 10 Vehicle Makes"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------
# Vehicle Type Distribution
# ---------------------------------------

vehicle_type_df = pd.read_sql(
    """
    SELECT vehicle_type,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY vehicle_type
    ORDER BY total DESC
    """
    ,
    engine
)

fig2 = px.pie(
    vehicle_type_df,
    names="vehicle_type",
    values="total",
    title="Vehicle Type Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------
# Vehicle Year Distribution
# ---------------------------------------

year_df = pd.read_sql(
    """
    SELECT year,
           COUNT(*) AS total
    FROM traffic_violations
    WHERE year IS NOT NULL
    GROUP BY year
    ORDER BY year
    """,
    engine
)

fig3 = px.histogram(
    year_df,
    x="year",
    y="total",
    title="Vehicle Year Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

st.download_button(
    label="📥 Download Vehicle Analysis CSV",
    data=vehicle_df.to_csv(index=False),
    file_name="vehicle_analysis.csv",
    mime="text/csv"
)