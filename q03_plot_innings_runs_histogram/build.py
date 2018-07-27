# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    inning_runs1=ipl_df.loc[ipl_df['inning']==1,['match_code','total']]
    inning_runs1=inning_runs1.groupby(['match_code'])['total'].sum()
    inning_runs2=ipl_df.loc[ipl_df['inning']==2,['match_code','total']]
    inning_runs2=inning_runs2.groupby(['match_code'])['total'].sum()
    plt.subplot(121)
    plt.hist(inning_runs1)
    plt.subplot(122)
    plt.hist(inning_runs2)
plot_innings_runs_histogram()


