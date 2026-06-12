import streamlit as st

st.title("AI Construction Assistant")

question = st.text_input("Ask a construction question")

if question:
    if "steel weight" in question.lower():
        st.write("Steel Weight = D²/162 kg/m")
    elif "cube test" in question.lower():
        st.write("Cube test is conducted at 7 and 28 days.")
    else:
        st.write("Construction query receivedimport streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Agent for Construction",
    page_icon="🏗️",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏗️ Construction AI Agent")

module = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Concrete Calculator",
        "Steel Calculator",
        "Cube Test Checker",
        "BOQ Generator",
        "Quality Checklist"
    ]
)

# Dashboard
if module == "Dashboard":

    st.title("🏗️ AI Agent for Construction")

    st.markdown("### Construction Management & Site Engineering Assistant")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects", "12")

    with col2:
        st.metric("BOQ Generated", "58")

    with col3:
        st.metric("Cube Tests", "142")

    with col4:
        st.metric("Inspections", "87")

    st.divider()

    st.subheader("Available Modules")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("Concrete Quantity Calculator")

    with c2:
        st.info("Steel Weight Calculator")

    with c3:
        st.info("Cube Test Checker")

# Concrete Calculator
elif module == "Concrete Calculator":

    st.title("🧱 Concrete Quantity Calculator")

    col1, col2, col3 = st.columns(3)

    with col1:
        length = st.number_input("Length (m)", min_value=0.0)

    with col2:
        width = st.number_input("Width (m)", min_value=0.0)

    with col3:
        depth = st.number_input("Depth (m)", min_value=0.0)

    if st.button("Calculate Concrete Quantity"):

        volume = length * width * depth

        st.success(f"Required Concrete = {volume:.3f} m³")

# Steel Calculator
elif module == "Steel Calculator":

    st.title("🔩 Steel Weight Calculator")

    dia = st.number_input(
        "Bar Diameter (mm)",
        min_value=6,
        max_value=40
    )

    length = st.number_input(
        "Bar Length (m)",
        min_value=0.0
    )

    if st.button("Calculate Steel Weight"):

        weight = (dia * dia / 162) * length

        st.success(
            f"Steel Weight = {weight:.2f} kg"
        )

# Cube Test
elif module == "Cube Test Checker":

    st.title("🧪 Cube Test Checker")

    grade = st.selectbox(
        "Concrete Grade",
        ["M20", "M25", "M30", "M35", "M40"]
    )

    strength = st.number_input(
        "28-Day Strength (MPa)",
        min_value=0.0
    )

    if st.button("Check Cube Result"):

        grades = {
            "M20": 20,
            "M25": 25,
            "M30": 30,
            "M35": 35,
            "M40": 40
        }

        if strength >= grades[grade]:
            st.success("PASS ✅")
        else:
            st.error("FAIL ❌")

# BOQ Generator
elif module == "BOQ Generator":

    st.title("📋 BOQ Generator")

    area = st.number_input(
        "Built-up Area (sqft)",
        min_value=0
    )

    if st.button("Generate BOQ"):

        boq = pd.DataFrame({
            "Item": [
                "Concrete",
                "Steel",
                "Brickwork",
                "Plastering"
            ],
            "Quantity": [
                round(area * 0.04, 2),
                round(area * 4, 2),
                round(area * 8, 2),
                round(area * 2.5, 2)
            ],
            "Unit": [
                "m³",
                "kg",
                "Nos",
                "m²"
            ]
        })

        st.dataframe(
            boq,
            use_container_width=True
        )

# Quality Checklist
elif module == "Quality Checklist":

    st.title("✅ Site Quality Inspection")

    checklist = [
        "Column Alignment Checked",
        "Rebar Cover Available",
        "Shuttering Clean",
        "Concrete Grade Verified",
        "Cube Samples Taken",
        "Slab Levels Checked"
    ]

    completed = 0

    for item in checklist:
        if st.checkbox(item):
            completed += 1

    percentage = completed / len(checklist) * 100

    st.progress(int(percentage))

    st.write(
        f"Inspection Completion : {percentage:.0f}%"
    )
