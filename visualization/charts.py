import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_signal_charts(results):

    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.10,
        subplot_titles=(
            "Heart Rate",
            "Blood Pressure",
            "Oxygen Saturation"
        )
    )

    # Heart rate
    fig.add_trace(
        go.Scatter(
            x=results["time"],
            y=results["heart_rate"],
            name="Heart Rate",
            mode="lines"
        ),
        row=1,
        col=1
    )

    # Blood pressure
    fig.add_trace(
        go.Scatter(
            x=results["time"],
            y=results["systolic_bp"],
            name="Systolic BP",
            mode="lines"
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=results["time"],
            y=results["diastolic_bp"],
            name="Diastolic BP",
            mode="lines"
        ),
        row=2,
        col=1
    )

    # Oxygen saturation
    fig.add_trace(
        go.Scatter(
            x=results["time"],
            y=results["spo2"],
            name="SpO2",
            mode="lines"
        ),
        row=3,
        col=1
    )

    fig.update_xaxes(title_text="Time (minutes)", row=3, col=1)

    fig.update_yaxes(title_text="Beats/min", row=1, col=1)
    fig.update_yaxes(title_text="mmHg", row=2, col=1)
    fig.update_yaxes(title_text="SpO2 (%)", row=3, col=1)

    fig.update_layout(
        title="Physiological Responses Over Time",
        height=850,
        hovermode="x unified",
        template="plotly_white"
    )

    return fig