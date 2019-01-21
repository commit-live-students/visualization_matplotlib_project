# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

def plot_innings_runs_histogram():
    inning_1 = ipl_df[ipl_df['inning'] == 1]
    inning_2 = ipl_df[ipl_df['inning'] == 2] 
    sum_innings_1 = inning_1['runs'].sum()
    sum_innings_2 = inning_2['runs'].sum()
    plt.hist(sum_innings_1, sum_innings_2)
plot_innings_runs_histogram()
inning_1 = ipl_df[ipl_df['inning'] == 1]
inning_2 = ipl_df[ipl_df['inning'] == 2]
inning_1 = batting_team.value_counts('1')
inning_2 = batting_team.value_counts('2')
#x_series = np.arange(len(deliveries_by_team.index))
#plt.bar(x_series, deliveries_by_team)
#plt.xticks(x_series, deliveries_by_team.index.values, rotation=90)
#plt.show()
inning_2['runs'].sum()

