import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    ipl_df1 = ipl_df[['match_code','inning','delivery','runs']]
    aggregator = {'delivery' : 'count',
                 'runs': 'sum'}
    runs = ipl_df1.groupby(['match_code','inning']).agg(aggregator).reset_index('match_code')
    x = runs[runs.index == 1]
    y = runs[runs.index == 2]
    x = x['runs']
    y = y['runs']
    fig, ax = plt.subplots()
    ax.hist(x)
    ax.hist(y)

    fig.show()
