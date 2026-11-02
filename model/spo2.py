import numpy as np


def calculate_spo2(time, baseline_spo2=98.0):
    """
    Calculate simulated oxygen saturation over time.

    SpO2 remains constant in this simplified model to illustrate
    that blood loss does not necessarily cause a reduction in
    measured oxygen saturation.
    """

    if not 0 < baseline_spo2 <= 100:
        raise ValueError("SpO2 must be greater than 0 and at most 100.")

    spo2 = np.full_like(
        time,
        fill_value=baseline_spo2,
        dtype=float
    )

    return spo2