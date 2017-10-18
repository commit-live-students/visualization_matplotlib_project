# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():
    fig,ax=plt.subplots(nrows=1,ncols=2)
    s1=ipl_df[ipl_df['inning']==1]
    s2=ipl_df[ipl_df['inning']==2]
    ax[0].hist(s1['runs'],bins=10)
    ax[1].hist(s2['runs'],bins=10)
    plt.show()

plot_innings_runs_histogram()
