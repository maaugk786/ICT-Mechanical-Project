import streamlit as st

# 1. Page Configuration - Wide layout for a dashboard feel
st.set_page_config(
    page_title="MECH-PRO Dashboard",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #4a4e69;
    }
    div[data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_with_html_view=True)

# --- SIDEBAR: Developer Branding ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1085/1085803.png", width=100)
    st.title("MECH-PRO v2.0")
    st.markdown("---")
    st.subheader("👨‍💻 Developer Profile")
    st.info(f"**Name:** Muhammad Bilal\n\n**Roll:** 25-ME-124")
    st.markdown("---")
    st.caption("UET Taxila | Mechanical Engineering")

# --- MAIN INTERFACE ---
st.title("🛠️ Mechanical Engineering Smart Dashboard")
st.write("An all-in-one utility for rapid material analysis and unit synchronization.")

# Creating sleek Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["🚀 Unit Converter", "⚖️ Material Density", "📋 Project Docs"])

# --- TAB 1: UNIT CONVERTER ---
with tab1:
    st.subheader("Smart Unit Conversion")
    col_input, col_arrow, col_output = st.columns([2, 1, 2])
    
    with col_input:
        cat = st.selectbox("Select Parameter", ["Pressure (Bar → Pa)", "Power (HP → Watts)", "Force (N → Lbf)"])
        val = st.number_input("Input Magnitude", value=1.0, step=0.1, key="conv_input")
    
    with col_arrow:
        st.markdown("<h2 style='text-align: center; padding-top: 25px;'>➔</h2>", unsafe_with_html_view=True)
        
    with col_output:
        if "Pressure" in cat:
            res = val * 100000
            st.metric("Resulting Pascal (Pa)", f"{res:,.0f} Pa")
        elif "Power" in cat:
            res = val * 745.7
            st.metric("Resulting Watts (W)", f"{res:,.2f} W")
        else:
            res = val * 0.2248
            st.metric("Resulting Pound-force (lbf)", f"{res:,.4f} lbf")

# --- TAB 2: MATERIAL DENSITY & WEIGHT ---
with tab2:
    st.subheader("Material Intelligence")
    
    mat_db = {
        "Steel (Mild)": 7850,
        "Aluminum (6061)": 2700,
        "Copper (Pure)": 8960,
        "Titanium (Gr5)": 4500,
        "Stainless Steel": 8000
    }
    
    c1, c2 = st.columns(2)
    with c1:
        selected_mat = st.selectbox("Choose Material Profile", list(mat_db.keys()))
        density = mat_db[selected_mat]
        st.write(f"Standard Density: `{density} kg/m³`")
    
    with c2:
        vol = st.slider("Define Volume (m³)", 0.0, 10.0, 1.0)
        total_mass = vol * density
    
    # Large Display for Result
    st.divider()
    st.subheader("Estimated Mass Calculation")
    st.success(f"The total mass for **{vol} m³** of **{selected_mat}** is **{total_mass:,.2f} Kilograms**")
    
    # Small visualization hack (just for show)
    st.progress(min(vol/10, 1.0))

# --- TAB 3: PROJECT INFO ---
with tab3:
    st.markdown("""
    ### 📌 About This App
    This application is designed to streamline day-to-day calculations for mechanical engineers. 
    
    **Features Included:**
    - High-precision unit conversions.
    - Standardized material density database.
    - Real-time mass estimation based on volume.
    
    **Future Updates:**
    - [ ] Thermal expansion coefficients.
    - [ ] Stress-Strain curve generator.
    - [ ] CAD file metadata viewer.
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("<center>Built with ❤️ and Python for the 25-ME Batch</center>", unsafe_with_html_view=True)
