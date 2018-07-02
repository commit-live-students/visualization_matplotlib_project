# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    f_in = ipl_df[ipl_df['inning'] == 1]
    f_runs = f_in.groupby(['match_code','inning']).agg(sum)['runs']
    s_in = ipl_df[ipl_df['inning'] == 2]
    s_runs = s_in.groupby(['match_code','inning']).agg(sum)['runs']
    plt.hist(f_runs)
    plt.hist(s_runs)
    plt.show()
    
plot_innings_runs_histogram()




