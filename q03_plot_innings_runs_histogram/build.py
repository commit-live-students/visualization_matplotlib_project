# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    df = ipl_df.groupby(['match_code','inning'])['runs'].sum().reset_index()
    plt.hist(df['runs'][df['inning']==1], bins=50)
    plt.hist(df['runs'][df['inning']==2], bins=50)
    plt.show()
    return


# Solution
