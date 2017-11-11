# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    Y = ipl_df.groupby(['match_code','inning','batsman']).agg({'delivery': pd.Series.sum, 'runs':pd.Series.sum })
    fig,axes = plt.subplots(nrows=1, ncols=2)
    Y.plot.hist()
    plt.show()






# Solution
