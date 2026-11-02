
import numpy as np
import matplotlib.pyplot as plt

from model.disturbance import calculate_disturbance
from model.compensation import calculate_compensation
from model.heart_rate import calculate_heart_rate


# Generate the time points
time = np.linspace(0, 60, 300)

# Calculate the disturbance
disturbance = calculate_disturbance(
    time=time,
    onset_time=10,
    stabilization_time=40,
    maximum_level=0.8,
    progression_rate=0.12
)

# Calculate the compensatory response
response, excess = calculate_compensation(
    disturbance,
    capacity=0.4
)

# Calculate heart rate
heart_rate = calculate_heart_rate(
    compensatory_response=response,
    uncompensated_disturbance=excess,
    baseline_hr=75,
    compensation_gain=25,
    excess_gain=40
)

# Plot the simulated heart rate
plt.plot(time, heart_rate, label="Simulated heart rate")

plt.xlabel("Time (minutes)")
plt.ylabel("Heart rate (beats/min)")
plt.title("Simulated Heart Rate Response")

plt.legend()
plt.grid(True)
plt.show()
