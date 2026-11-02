
import numpy as np

from model.simulation import run_simulation


time = np.linspace(0, 60, 300)

scenarios = [
    {"maximum_level": 0.3, "capacity": 0.4},
    {"maximum_level": 0.6, "capacity": 0.4},
    {"maximum_level": 0.8, "capacity": 0.4},
    {"maximum_level": 0.8, "capacity": 0.2},
    {"maximum_level": 1.0, "capacity": 0.7},
]

for number, parameters in enumerate(scenarios, start=1):

    results = run_simulation(
        time=time,
        **parameters
    )

    assert np.isfinite(
        results.select_dtypes(include="number").to_numpy()
    ).all()

    assert (results["heart_rate"] > 0).all()

    assert (
        results["systolic_bp"] > results["diastolic_bp"]
    ).all()

    assert (
        results["spo2"].between(0, 100)
    ).all()

    assert np.all(np.diff(results["disturbance"]) >= -1e-10)

    print(f"Scenario {number}: passed")

print("\nAll model tests passed.")
