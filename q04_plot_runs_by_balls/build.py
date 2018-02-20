import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    group_by = ipl_df.groupby(["match_code", "batsman"])
    balls = group_by['runs'].count().rename('balls').reset_index()
    runs = group_by['runs'].sum().rename('runs').reset_index()
    df = pd.merge(balls, runs, on=['match_code', 'batsman'])
    plt.scatter(x=df['runs'], y=df['balls'])
    plt.xlabel('Count of Balls Played')
    plt.ylabel('Total Runs Scored')
    plt.show()

# Solution
