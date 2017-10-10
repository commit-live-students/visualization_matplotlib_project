# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():

    fil1=ipl_df['inning']==1
    fil2=ipl_df['inning']==2
    x=ipl_df[fil1].groupby('match_code')['runs'].sum()
    y=ipl_df[fil2].groupby('match_code')['runs'].sum()


    fig, axes = plt.subplots(nrows=1,ncols=2)
    axes[0].hist(x)
    axes[1].hist(y)
    plt.show()
# Solution

#plot_innings_runs_histogram()
