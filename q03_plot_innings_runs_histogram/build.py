# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    df1 = ipl_df[ipl_df['inning'] == 1].groupby(by = ('match_code','inning'))['runs'].sum()   
    df2 = ipl_df[ipl_df['inning'] == 2].groupby(by = ('match_code','inning'))['runs'].sum()   
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].hist(df1)
    axes[1].hist(df2)
    plt.show()
# Solution
plot_innings_runs_histogram()


