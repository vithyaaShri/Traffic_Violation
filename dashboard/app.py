import streamlit as st

st.set_page_config(
    page_title="Traffic Violations Insight System",
    layout="wide"
)

st.title("🚦 Traffic Violations Insight System")
st.write("Traffic Violations Analysis Dashboard")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1506521781263-d8422e82f27a?w=800&q=80",
        use_container_width=True,
        caption="Road Safety & Traffic Analysis"
    )

with col2:
    st.markdown("## 📊 About This Dashboard")
    st.markdown("""
    This system provides comprehensive insights into traffic violations data including:
    
    - 🔍 **Overview** — Key metrics and summaries
    - ⚠️ **Violation Analysis** — Types and trends
    - 🚗 **Vehicle Analysis** — Vehicle-wise breakdown
    - 👥 **Demographic Analysis** — Driver demographics
    - 🗺️ **Geographic Analysis** — Location-based patterns
    """)
    st.info("👈 Use the sidebar to navigate between sections")