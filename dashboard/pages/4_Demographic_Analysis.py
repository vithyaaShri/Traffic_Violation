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
st.title("👥 Demographic Analysis")

# Gender Analysis
st.subheader("Gender Distribution")

gender_df = pd.read_sql(
    """
    SELECT gender,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY gender
    """,
    engine
)

fig1 = px.pie(
    gender_df,
    names="gender",
    values="total",
    title="Violations by Gender"
)

st.plotly_chart(fig1, use_container_width=True)

# Race Analysis
st.subheader("Race Distribution")

race_df = pd.read_sql(
    """
    SELECT race,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY race
    ORDER BY total DESC
    """,
    engine
)

fig2 = px.bar(
    race_df,
    x="race",
    y="total",
    title="Violations by Race"
)

st.plotly_chart(fig2, use_container_width=True)

# Driver State Analysis
st.subheader("Top Driver States")

state_df = pd.read_sql(
    """
    SELECT driver_state,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY driver_state
    ORDER BY total DESC
    LIMIT 10
    """,
    engine
)

fig3 = px.bar(
    state_df,
    x="driver_state",
    y="total",
    title="Top 10 Driver States"
)

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(state_df)
st.download_button(
    label="📥 Download Demographic Data",
    data=state_df.to_csv(index=False),
    file_name="demographic_analysis.csv",
    mime="text/csv"
)