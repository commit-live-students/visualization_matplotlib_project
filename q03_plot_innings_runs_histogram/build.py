# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    plt.figure()
    plt.subplot(1,2,1)
    inning1_dist=ipl_df[ipl_df['inning']==1].groupby(['match_code'])['runs'].sum()
    inning1_dist.plot(kind='hist')
    
    plt.subplot(1,2,2)
    inning2_dist=ipl_df[ipl_df['inning']==2].groupby(['match_code'])['runs'].sum()
    inning2_dist.plot(kind='hist')
    plt.show();
plot_innings_runs_histogram()



