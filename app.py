import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# Header Section with Student Details
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")
st.markdown("---")
st.sidebar.header("Developer Information")
st.sidebar.write("**Name:** Muhammad Abdullah Asad")
st.sidebar.write("**Roll Number:** 25-ME-020")

# Main Navigation
option = st.selectbox("Choose a Tool", ["Unit Converter", "Material Density Checker"])

# --- TOOL 1: UNIT CONVERTER ---
if option == "Unit Converter":
    st.header("Unit Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.radio("Select Category", ["Pressure", "Power", "Force"])
        value = st.number_input("Enter Value", value=1.0)

    with col2:
        if category == "Pressure":
            # Bar to Pascal
            result = value * 100000
            st.metric("Pascal (Pa)", f"{result:,.2f}")
            st.info("Conversion: 1 Bar = 100,000 Pa")
            
        elif category == "Power":
            # HP to Watts
            result = value * 745.7
            st.metric("Watts (W)", f"{result:,.2f}")
            st.info("Conversion: 1 HP = 745.7 W")
            
        elif category == "Force":
            # Newton to Pound-force
            result = value * 0.2248
            st.metric("Pound-force (lbf)", f"{result:,.4f}")
            st.info("Conversion: 1 N ≈ 0.2248 lbf")

# --- TOOL 2: DENSITY CHECKER ---
else:
    st.header("Material Density Checker")
    
    # Standard engineering materials density in kg/m^3
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Water": 1000
    }
    
    material = st.selectbox("Select Material", list(densities.keys()))
    
    st.write(f"The density of **{material}** is approximately:")
    st.success(f"{densities[material]} kg/m³")
    
    # Weight Calculator
    st.subheader("Quick Weight Estimator")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0)
    weight = volume * densities[material]
    st.write(f"Estimated Mass: **{weight:,.2f} kg**")

# Footer
st.markdown("---")
st.caption("Developed for Mechanical Engineering Department Portfolio.")
