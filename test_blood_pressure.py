
import numpy as np
import matplotlib.pyplot as plt

from model.disturbance import calculate_disturbance
from model.compensation import calculate_compensation
from model.blood_pressure import calculate_blood_pressure


time = np.linspace(0, 60, 300)

disturbance = calculate_disturbance(
    time=time,
    onset_time=10,
    stabilization_time=40,
    maximum_level=0.8,
    progression_rate=0.12
)

response, excess = calculate_compensation(
    disturbance,
    capacity=0.4
)

systolic_bp, diastolic_bp = calculate_blood_pressure(
    response,
    excess
)

plt.plot(time, systolic_bp, label="Systolic BP")
plt.plot(time, diastolic_bp, label="Diastolic BP")

plt.xlabel("Time (minutes)")
plt.ylabel("Blood pressure (mmHg)")
plt.title("Simulated Blood Pressure Response")

plt.legend()
plt.grid(True)
plt.show()
