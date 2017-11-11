# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    Y = ipl_df.groupby(['match_code','batsman']).agg({'delivery': pd.Series.count, 'runs': pd.Series.sum})
    plt.scatter(Y['delivery'], Y['runs'])
    plt.show()


# Solution
