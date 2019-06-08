# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    group_sum = ipl_df.groupby(['match_code','batsman']).sum().reset_index()
#     print(group_sum)
    group_count = ipl_df.groupby(['match_code','batsman']).count().reset_index()
#     inning1_df = group_sum[group_sum['batsman'] == 1]
# #     inning2_df = group_sum[group_sum['inning'] == 2]
# #     fig, axes = plt.subplots(1,2)
    plt.scatter(group_count['delivery'],group_sum['runs'])
# #     axes[1].scatter(inning2_df['runs'])
plot_runs_by_balls()
plt.show()

