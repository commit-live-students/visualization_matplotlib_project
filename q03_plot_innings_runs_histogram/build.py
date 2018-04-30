# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_innings_runs_histogram():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    first= ipl_df[ipl_df['inning']==1].groupby(['match_code']).agg({'runs':'sum'})
    sec= ipl_df[ipl_df['inning']==2].groupby(['match_code']).agg({'runs':'sum'})
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].plot(first.index,first['runs'])
    axes[1].plot(sec.index,sec['runs'])
    fig.show()


plot_innings_runs_histogram()
# Solution







