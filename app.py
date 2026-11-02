
import streamlit as st
import numpy as np

from model.simulation import run_simulation
from visualization.charts import create_signal_charts


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="PhysioSim",
    page_icon="🫀",
    layout="wide"
)


# --------------------------------------------------
# Introduction
# --------------------------------------------------

st.title("PhysioSim")

st.subheader(
    "Exploring physiological responses through simulation"
)

st.markdown("""
PhysioSim is an educational project exploring how selected
physiological signals respond to a hypothetical blood-loss
disturbance over time.

Adjust the parameters and observe how heart rate, blood pressure,
and oxygen saturation change in the model.
""")

st.divider()


# --------------------------------------------------
# Simulation controls
# --------------------------------------------------

st.sidebar.title("Simulation Controls")

st.sidebar.markdown(
    "Adjust the parameters to explore different scenarios."
)

onset_time = st.sidebar.slider(
    "Disturbance onset (minutes)",
    0, 30, 10
)

stabilization_time = st.sidebar.slider(
    "Stabilization time (minutes)",
    31, 60, 40
)

maximum_level = st.sidebar.slider(
    "Asymptotic disturbance level",
    0.1, 1.0, 0.8, 0.05
)

progression_rate = st.sidebar.slider(
    "Progression rate",
    0.01, 0.30, 0.12, 0.01
)

capacity = st.sidebar.slider(
    "Illustrative compensatory capacity",
    0.1, 0.9, 0.4, 0.05
)


# --------------------------------------------------
# Run simulation
# --------------------------------------------------

time = np.linspace(0, 60, 300)

results = run_simulation(
    time=time,
    onset_time=onset_time,
    stabilization_time=stabilization_time,
    maximum_level=maximum_level,
    progression_rate=progression_rate,
    capacity=capacity
)


# --------------------------------------------------
# Key outputs
# --------------------------------------------------

st.header("Simulation Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Peak heart rate",
        f"{results['heart_rate'].max():.1f} bpm"
    )

with col2:
    st.metric(
        "Lowest systolic pressure",
        f"{results['systolic_bp'].min():.1f} mmHg"
    )

with col3:
    st.metric(
        "Modelled SpO₂",
        f"{results['spo2'].iloc[-1]:.1f}%"
    )


# --------------------------------------------------
# Physiological charts
# --------------------------------------------------

st.header("Physiological Signals")

st.plotly_chart(
    create_signal_charts(results),
    use_container_width=True
)


# --------------------------------------------------
# Scientific explanations
# --------------------------------------------------

st.header("Understanding the Model")

with st.expander("Heart Rate"):
    st.write("""
    Heart rate increases in response to the modelled compensatory
    response and uncompensated disturbance. This is a simplified
    representation of cardiovascular compensation.
    """)

with st.expander("Blood Pressure"):
    st.write("""
    The model initially represents compensation through a relatively
    stable systolic pressure and a slight rise in diastolic pressure.
    As compensatory capacity is exceeded, both pressures decline.
    """)

with st.expander("Oxygen Saturation"):
    st.write("""
    SpO₂ remains stable in this simulation. Blood loss can reduce
    total oxygen-carrying capacity and tissue oxygen delivery without
    necessarily reducing the percentage of haemoglobin saturated
    with oxygen.
    """)

with st.expander("Disturbance and Compensation"):
    st.write("""
    The disturbance is a normalized mathematical variable, not a
    percentage of blood volume lost. Compensatory capacity is an
    illustrative model parameter rather than a measured biological
    reserve.
    """)


# --------------------------------------------------
# Simulation data
# --------------------------------------------------

with st.expander("View Simulation Data"):
    st.dataframe(
        results.round(3),
        use_container_width=True
    )


# --------------------------------------------------
# Scientific limitations
# --------------------------------------------------

st.divider()

st.header("Scientific Limitations")

st.warning("""
PhysioSim is an educational conceptual model, not a diagnostic
or clinical prediction tool. Its equations and parameters are
illustrative and have not been calibrated or validated against
patient data. It does not represent every physiological response
to blood loss and must not be used to guide medical care.
""")

st.caption(
    "PhysioSim | An independent computational exploration "
    "of physiological responses."
)
