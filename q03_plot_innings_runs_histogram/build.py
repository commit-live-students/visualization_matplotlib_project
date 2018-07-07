# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():   
    df1=ipl_df[ipl_df['inning']==1]
    df2=ipl_df[ipl_df['inning']==2]
    df_1=df1.groupby(['match_code','inning',]).sum()
    df_2=df2.groupby(['match_code','inning',]).sum()
    plt.hist(df_1['runs'])
    plt.hist(df_2['runs'])
    plt.show()

