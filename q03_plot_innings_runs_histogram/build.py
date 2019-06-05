# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    hist1=ipl_df[ipl_df['inning']==1]
    hist2=ipl_df[ipl_df['inning']==2]
    
    sub1=hist1.groupby('match_code').sum()['runs']
    sub2=hist2.groupby('match_code').sum()['runs']

    fig,axes=plt.subplots(1,2)
    axes[0].hist(sub1)
    axes[1].hist(sub2)
    
    

