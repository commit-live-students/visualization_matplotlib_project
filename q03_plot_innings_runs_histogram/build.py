# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    #print(ipl_df.columns)
    table = ipl_df.groupby(['match_code','inning'])['total'].sum()
    #xLables = ipl_df['match_code'].unique()
    #print(table)
    firstInnings = table[:,1]
    secondInnings = table[:,2]
    #xLables = table.index.get_level_values(0)
    #print(len(xLables))
    #print(len(firstInnings.values))
    #print(secondInnings.values)
    fig, axes = plt.subplots(1,2)
    axes[0].hist(firstInnings.values)
    axes[1].hist(secondInnings.values)
    #plt.show()



