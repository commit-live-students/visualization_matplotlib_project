# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df_s=ipl_df.groupby(['match_code','batsman']).sum()
    df_c=ipl_df.groupby(['match_code','batsman']).count()
    plt.scatter(df_c['delivery'],df_s['runs'])
    plt.show()

plot_innings_runs_histogram()


