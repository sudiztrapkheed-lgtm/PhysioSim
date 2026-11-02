
import numpy as np


def calculate_compensation(disturbance, capacity):
    """
    Calculate the normalized compensatory response and
    the disturbance exceeding the assumed capacity.
    """

    if not 0 < capacity <= 1:
        raise ValueError("Capacity must be greater than 0 and at most 1.")

    compensatory_response = np.minimum(
        disturbance / capacity,
        1.0
    )

    uncompensated_disturbance = np.maximum(
        disturbance - capacity,
        0.0
    )

    return compensatory_response, uncompensated_disturbance
