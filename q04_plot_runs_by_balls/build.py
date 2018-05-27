# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    left = ipl_df.groupby(ipl_df['batsman']).agg(sum)
    right = ipl_df.groupby(ipl_df['batsman']).count()
    rel_df = left['runs'].to_frame().join(right['delivery'].to_frame(), how='inner')
    plt.scatter(rel_df['delivery'],rel_df['runs'])
    plt.title('Runs players make in how many balls')
    plt.xlabel('Balls Played')
    plt.ylabel('Runs Scored ')
    plt.show()

