
import streamlit as st

st.set_page_config(
    page_title="PhysioSim | Methodology",
    page_icon="🧪",
    layout="wide"
)

st.title("Model Methodology")

st.markdown("""
PhysioSim uses simplified mathematical relationships to explore
how a hypothetical blood-loss disturbance may influence selected
physiological signals over time.

The model combines established physiological concepts with
illustrative equations developed for this project.
""")

st.divider()

st.header("1. Disturbance Progression")

st.latex(r"D(t)=L(1-e^{-k\tau})")

st.markdown("""
- **L:** Asymptotic disturbance level.
- **k:** Progression rate.
- **τ:** Elapsed time since onset, limited at stabilization.

The disturbance is normalized, not a percentage of blood volume lost.
""")

st.header("2. Compensation")

st.latex(r"C(t)=\min\left(\frac{D(t)}{R},1\right)")
st.latex(r"E(t)=\max(D(t)-R,0)")

st.markdown("""
- **C:** Normalized compensatory response.
- **E:** Disturbance exceeding the assumed capacity.
- **R:** Illustrative compensatory capacity.
""")

st.header("3. Heart Rate")

st.latex(r"HR=HR_0+G_cC+G_eE")

st.markdown("""
The model uses a baseline heart rate and illustrative gains
to represent the influence of compensation and uncompensated
disturbance.
""")

st.header("4. Blood Pressure")

st.latex(r"SBP=SBP_0-G_sE^p")
st.latex(r"DBP=DBP_0+G_dC-G_eE^p")

st.markdown("""
These phenomenological equations represent an initial
compensatory phase followed by declining blood pressure.
They are not derived from a complete haemodynamic model.
""")

st.header("5. Oxygen Saturation")

st.latex(r"SpO_2(t)=98\%")

st.markdown("""
SpO₂ is held constant in this version to illustrate that oxygen
saturation does not measure total haemoglobin or total oxygen
delivery. Blood loss can reduce oxygen-carrying capacity even
when saturation remains relatively normal.
""")

st.divider()

st.header("Scientific Basis")

st.markdown("""
The physiological concepts informing this project include:

- **Hemorrhage and compensation:** Blood loss activates cardiovascular
  compensatory mechanisms, including increased heart rate and
  peripheral vasoconstriction. As compensation becomes insufficient,
  blood pressure can decline.

- **Oxygen transport:** Oxygen delivery depends on more than
  haemoglobin saturation; the amount of circulating haemoglobin
  also matters.

- **Pulse oximetry:** SpO₂ estimates the proportion of haemoglobin
  saturated with oxygen. It does not directly measure haemoglobin
  concentration or tissue oxygen delivery.
""")

st.header("References")

st.markdown("""
1. [Physiology of Human Hemorrhage and Compensation.
   Comprehensive Physiology (2021).](https://pubmed.ncbi.nlm.nih.gov/33577122/)

2. [Hemorrhagic Shock. StatPearls, NCBI Bookshelf.](https://www.ncbi.nlm.nih.gov/books/NBK470382/)

3. [Pulse oximetry: Understanding its basic principles
   facilitates appreciation of its limitations.
   Respiratory Medicine (2013).](https://pubmed.ncbi.nlm.nih.gov/23490227/)

4. [British Thoracic Society Guideline for Oxygen Use
   in Adults in Healthcare and Emergency Settings (2017).](https://doi.org/10.1136/thoraxjnl-2016-209729)
""")

st.divider()

st.header("Assumptions and Limitations")

st.markdown("""
- The model represents one hypothetical individual.
- All numerical gains and parameters are illustrative.
- The equations are not calibrated against patient data.
- Individual physiological responses vary.
- The model does not represent every stage of haemorrhagic shock.
- Stabilization of the disturbance does not imply physiological recovery.
- The simulation is not a diagnostic or treatment tool.
""")

st.info(
    "PhysioSim is an independent educational computational project. "
    "Its purpose is to explore physiological relationships, not "
    "to predict clinical outcomes."
)
