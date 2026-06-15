import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
# from utils.database_connection import get_engine
import plotly.express as px

# --------------------------------------------------
# Database Connection
# --------------------------------------------------

USERNAME = "root"
PASSWORD = "root"
DATABASE = "traffic_violation_db"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)


# engine = get_engine()
# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Overview",
    layout="wide"
)

st.title("📊 Traffic Violations Dashboard Overview")

# --------------------------------------------------
# KPI Queries
# --------------------------------------------------

total_violations = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_violations",
    engine
)

total_accidents = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_violations WHERE accident = TRUE",
    engine
)

alcohol_cases = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_violations WHERE alcohol = TRUE",
    engine
)

search_cases = pd.read_sql(
    "SELECT COUNT(*) AS total FROM traffic_violations WHERE search_conducted = TRUE",
    engine
)

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Violations",
        f"{total_violations.iloc[0,0]:,}"
    )

with col2:
    st.metric(
        "Total Accidents",
        f"{total_accidents.iloc[0,0]:,}"
    )

with col3:
    st.metric(
        "Alcohol Cases",
        f"{alcohol_cases.iloc[0,0]:,}"
    )

with col4:
    st.metric(
        "Search Conducted",
        f"{search_cases.iloc[0,0]:,}"
    )

# --------------------------------------------------
# Monthly Trend
# --------------------------------------------------

st.subheader("📈 Monthly Violation Trend")

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

fig = px.line(
    monthly_df,
    x="month",
    y="total",
    markers=True,
    title="Monthly Violations Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# Top 10 Violation Types
# --------------------------------------------------

st.subheader("🚨 Top 10 Violation Types")

top_violation_df = pd.read_sql(
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

fig2 = px.bar(
    top_violation_df,
    x="violation_type",
    y="total",
    title="Top 10 Violation Types"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)