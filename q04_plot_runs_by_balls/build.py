# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    sum_of_runs = ipl_df.groupby(['match_code','batsman'])['runs'].agg('sum')
    count_of_balls = ipl_df.groupby(['match_code','batsman'])['delivery'].agg('count')
    plt.scatter(count_of_balls,sum_of_runs)
    plt.show()
sum_of_runs = ipl_df.groupby(['match_code','batsman'])['runs'].agg('sum')
count_of_balls = ipl_df.groupby(['match_code','batsman'])['delivery'].agg('count')
plot_runs_by_balls()


