
import numpy as np


def calculate_disturbance(
    time,
    onset_time,
    stabilization_time,
    maximum_level,
    progression_rate
):
    """
    Calculate a normalized disturbance that increases over time
    and remains constant after stabilization.
    """

    if stabilization_time <= onset_time:
        raise ValueError("Stabilization time must be after onset time.")

    if not 0 <= maximum_level <= 1:
        raise ValueError("Maximum level must be between 0 and 1.")

    if progression_rate <= 0:
        raise ValueError("Progression rate must be positive.")

    elapsed_time = np.clip(
        time - onset_time,
        0,
        stabilization_time - onset_time
    )

    disturbance = maximum_level * (
        1 - np.exp(-progression_rate * elapsed_time)
    )

    return disturbance
