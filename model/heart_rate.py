
def calculate_heart_rate(
    compensatory_response,
    uncompensated_disturbance,
    baseline_hr=75,
    compensation_gain=25,
    excess_gain=40
):
    """
    Calculate simulated heart rate from the modelled
    compensatory response and uncompensated disturbance.

    All gains are illustrative model parameters,
    not clinically calibrated values.
    """

    if baseline_hr <= 0:
        raise ValueError("Baseline heart rate must be positive.")

    if compensation_gain < 0 or excess_gain < 0:
        raise ValueError("Heart-rate gains cannot be negative.")

    heart_rate = (
        baseline_hr
        + compensation_gain * compensatory_response
        + excess_gain * uncompensated_disturbance
    )

    return heart_rate
