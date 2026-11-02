import numpy as np
import pandas as pd

from model.disturbance import calculate_disturbance
from model.compensation import calculate_compensation
from model.heart_rate import calculate_heart_rate
from model.blood_pressure import calculate_blood_pressure
from model.spo2 import calculate_spo2


def run_simulation(
    time,
    onset_time=10,
    stabilization_time=40,
    maximum_level=0.8,
    progression_rate=0.12,
    capacity=0.4
):
    """
    Run the complete physiological simulation.

    Returns a DataFrame containing the modelled disturbance,
    compensatory response, and physiological signals.
    """

    disturbance = calculate_disturbance(
        time,
        onset_time,
        stabilization_time,
        maximum_level,
        progression_rate
    )

    compensatory_response, uncompensated_disturbance = (
        calculate_compensation(
            disturbance,
            capacity
        )
    )

    heart_rate = calculate_heart_rate(
        compensatory_response,
        uncompensated_disturbance
    )

    systolic_bp, diastolic_bp = calculate_blood_pressure(
        compensatory_response,
        uncompensated_disturbance
    )

    spo2 = calculate_spo2(time)

    results = pd.DataFrame({
        "time": time,
        "disturbance": disturbance,
        "compensatory_response": compensatory_response,
        "uncompensated_disturbance": uncompensated_disturbance,
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "spo2": spo2
    })

    return results