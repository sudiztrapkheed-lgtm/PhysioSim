
import numpy as np
import matplotlib.pyplot as plt

from model.disturbance import calculate_disturbance
from model.compensation import calculate_compensation


time = np.linspace(0, 60, 300)

disturbance = calculate_disturbance(
    time=time,
    onset_time=10,
    stabilization_time=40,
    maximum_level=0.8,
    progression_rate=0.12
)

# Calculate the response using an assumed capacity
capacity = 0.4

response, excess = calculate_compensation(
    disturbance,
    capacity
)

plt.plot(time, disturbance, label="Disturbance")
plt.plot(time, response, label="Compensatory response")
plt.plot(time, excess, label="Uncompensated disturbance")

plt.xlabel("Time (minutes)")
plt.ylabel("Normalized model values")
plt.title("Disturbance and Compensatory Response")

plt.legend()
plt.grid(True)
plt.show()
