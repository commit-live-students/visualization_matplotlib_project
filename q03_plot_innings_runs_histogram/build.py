# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df_inning1 = ipl_df[ipl_df['inning'] == 1].groupby(('match_code','inning'))['runs'].sum()   
    df_inning2 = ipl_df[ipl_df['inning'] == 2].groupby(('match_code','inning'))['runs'].sum()   
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].hist(df_inning1)
    axes[1].hist(df_inning2)
plt.show()
#plot_innings_runs_histogram()    


