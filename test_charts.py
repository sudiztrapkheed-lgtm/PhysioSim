import numpy as np

from model.simulation import run_simulation
from visualization.charts import create_signal_charts


time = np.linspace(0, 60, 300)

results = run_simulation(time)

fig = create_signal_charts(results)

fig.show()