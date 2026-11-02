import numpy as np
import matplotlib.pyplot as plt

from model.spo2 import calculate_spo2


time = np.linspace(0, 60, 300)

spo2 = calculate_spo2(
    time=time,
    baseline_spo2=98.0
)

plt.plot(time, spo2, label="SpO2")

plt.xlabel("Time (minutes)")
plt.ylabel("Oxygen saturation (%)")
plt.title("Simulated Oxygen Saturation")

plt.ylim(90, 100)
plt.legend()
plt.grid(True)
plt.show()