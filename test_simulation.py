import numpy as np

from model.simulation import run_simulation


time = np.linspace(0, 60, 300)

results = run_simulation(time)

print("\nFirst five rows:")
print(results.head())

print("\nLast five rows:")
print(results.tail())

print("\nSimulation summary:")
print(results.describe())