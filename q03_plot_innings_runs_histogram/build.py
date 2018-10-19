# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    ipl_df1 = ipl_df[['match_code','inning','runs']].groupby(['match_code','inning']).sum()
    fig, axes = plt.subplots(nrows=1, ncols=2)
    plt.hist(ipl_df1['runs'])
#     plt.title('Deliveries Played')
#     plt.xlabel('Teams')
#     plt.ylabel('Deliveries')
    plt.show()
    
plot_innings_runs_histogram()

