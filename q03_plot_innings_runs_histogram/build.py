# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    fig, axes = plt.subplots(nrows=1, ncols=2)
    new_data1 = ipl_df[ipl_df['inning']==1].groupby(['match_code','batsman']).agg({'delivery':'count', 'runs':'sum'})
    new_data2 = ipl_df[ipl_df['inning']==2].groupby(['match_code','batsman']).agg({'delivery':'count', 'runs':'sum'})
    x1=new_data1.index
    x2=new_data2.index
    y1=new_data1['runs']
    y2=new_data2['runs']
    axes[0].hist(y1, bins=10)
    axes[1].hist(y2, bins=10)
    fig.show()

