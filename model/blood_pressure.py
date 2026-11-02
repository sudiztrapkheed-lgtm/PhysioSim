
import numpy as np


def calculate_blood_pressure(
    compensatory_response,
    uncompensated_disturbance,
    baseline_sbp=120,
    baseline_dbp=80,
    systolic_gain=35,
    diastolic_compensation_gain=6,
    diastolic_decline_gain=35,
    decline_exponent=1.2
):
    """
    Calculate simulated systolic and diastolic blood pressure.

    Parameters are illustrative and are not clinically calibrated.
    """

    if baseline_sbp <= baseline_dbp:
        raise ValueError("Systolic pressure must exceed diastolic pressure.")

    if min(
        systolic_gain,
        diastolic_compensation_gain,
        diastolic_decline_gain
    ) < 0:
        raise ValueError("Response gains cannot be negative.")

    if decline_exponent <= 0:
        raise ValueError("Decline exponent must be positive.")

    pressure_decline = np.power(
        uncompensated_disturbance,
        decline_exponent
    )

    systolic_bp = (
        baseline_sbp
        - systolic_gain * pressure_decline
    )

    diastolic_bp = (
        baseline_dbp
        + diastolic_compensation_gain * compensatory_response
        - diastolic_decline_gain * pressure_decline
    )

    return systolic_bp, diastolic_bp
