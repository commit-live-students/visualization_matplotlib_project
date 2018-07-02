# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():   
    first= ipl_df[ipl_df['inning']==1].groupby(['match_code']).agg({'runs':'sum'})
    sec= ipl_df[ipl_df['inning']==2].groupby(['match_code']).agg({'runs':'sum'})
    plt.hist(first['runs'])
    plt.hist(sec['runs'])
    plt.show()

