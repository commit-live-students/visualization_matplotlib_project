# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    group_sum = ipl_df.groupby(['match_code', 'batsman']).sum().reset_index()
    runs=group_sum['runs']
    balls=group_sum['delivery']
    plt.scatter(balls,runs)
    plt.title('Runs scored for total balls played')
    plt.xlabel('Balls')
    plt.ylabel('Runs')
    plt.show();
plot_innings_runs_histogram() 





  




