import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
# from utils.database_connection import get_engine
import plotly.express as px

# ---------------------------------------
# Database Connection
# ---------------------------------------

USERNAME = "root"
PASSWORD = "root"
DATABASE = "traffic_violation_db"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)
# engine = get_engine()
st.title("🚨 Violation Analysis")

# ---------------------------------------
# Top Violation Types
# ---------------------------------------

st.subheader("Top Violation Types")

violation_df = pd.read_sql(
    """
    SELECT violation_type,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY violation_type
    ORDER BY total DESC
    LIMIT 10
    """,
    engine
)

fig1 = px.bar(
    violation_df,
    x="violation_type",
    y="total",
    title="Top 10 Violation Types"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------
# Monthly Trend
# ---------------------------------------

st.subheader("Monthly Violation Trend")

monthly_df = pd.read_sql(
    """
    SELECT month,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY month
    ORDER BY month
    """,
    engine
)

fig2 = px.line(
    monthly_df,
    x="month",
    y="total",
    markers=True,
    title="Monthly Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------
# Day Wise Analysis
# ---------------------------------------

st.subheader("Day Wise Analysis")

day_df = pd.read_sql(
    """
    SELECT day,
           COUNT(*) AS total
    FROM traffic_violations
    GROUP BY day
    ORDER BY total DESC
    """,
    engine
)

fig3 = px.pie(
    day_df,
    names="day",
    values="total",
    title="Violations by Day"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------
# Violation Type Table
# ---------------------------------------

st.subheader("Violation Summary Table")

st.dataframe(violation_df)
st.download_button(
    label="📥 Download Top Violations CSV",
    data=violation_df.to_csv(index=False),
    file_name="top_violations.csv",
    mime="text/csv"
)