import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs = ipl_df.groupby(['match_code','batsman'])
    run = DataFrame(runs.sum()['runs'])
    ball = DataFrame(runs.count()['delivery'])
    result = run.join(ball)
    result.plot(kind='scatter',y='runs',x='delivery')
    plt.show()
