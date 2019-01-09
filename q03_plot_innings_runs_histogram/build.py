# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    ipl_df1=ipl_df.groupby(['inning','match_code'], as_index=False)['runs'].sum()
    fig,axs=plt.subplots(1,2)
    axs[0].hist(ipl_df1[ipl_df1.inning==1].runs)
    axs[0].set_title('First Inning runs distribution')
    axs[1].hist(ipl_df1[ipl_df1.inning==2].runs)
    axs[1].set_title('Second Inning runs distribution')
    plt.show()
    fig
fig
ipl_df1=ipl_df.groupby(['inning','match_code'], as_index=False)['runs'].sum()
ipl_df1
ipl_df1[ipl_df1.inning==1].runs
ipl_df1[ipl_df1.inning==2].runs
fig,axs=plt.subplots(1,2)
axs[0].hist(ipl_df1[ipl_df1.inning==1].runs)
axs[0].set_title('First Inning runs distribution')
axs[1].hist(ipl_df1[ipl_df1.inning==2].runs)
axs[1].set_title('Second Inning runs distribution')
plt.show()
fig


