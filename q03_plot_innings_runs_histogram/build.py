# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():

    df = ipl_df[['match_code','inning', 'runs']].groupby(['match_code','inning']).sum().reset_index()
    plt.figure()
    plt.subplot(2, 1, 1)
    df[df['inning']==1]['runs'].plot.hist(bins=10)#, ax=ax1)
    plt.subplot(2, 1, 2)
    df[df['inning']==2]['runs'].plot.hist(bins=10)
    plt.show()


