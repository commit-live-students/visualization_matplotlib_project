# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df_all = ipl_df.groupby(['match_code','inning'])['runs'].agg('sum').reset_index()
    df1 = df_all[df_all['inning']==1]
    df1 = df1[['match_code','runs']]
    df2 = df_all[df_all['inning']==2]
    df2 = df2[['match_code','runs']]
    df1.plot.bar(x='match_code',y='runs')
    df2.plot.bar(x='match_code',y='runs')




