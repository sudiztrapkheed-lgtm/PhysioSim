
import numpy as np
import matplotlib.pyplot as plt

from model.disturbance import calculate_disturbance


# Create a time range from 0 to 60 minutes
time = np.linspace(0, 60, 300)

# Set the model parameters
disturbance = calculate_disturbance(
    time=time,
    onset_time=10,
    stabilization_time=40,
    maximum_level=0.8,
    progression_rate=0.12
)

# Plot the disturbance over time
plt.plot(time, disturbance)

plt.xlabel("Time (minutes)")
plt.ylabel("Normalized disturbance")
plt.title("Progression and Stabilization of Disturbance")

plt.ylim(0, 1)
plt.grid(True)
plt.show()
