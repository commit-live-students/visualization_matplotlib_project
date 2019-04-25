import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
        runs = ipl_df.groupby(['match_code','batsman','inning'])['runs'].sum()
        balls = ipl_df.groupby(['match_code','batsman'])['delivery'].count()
        plt.scatter(runs , balls)
        plt.xlabel('runs')
        plt.ylabel('count of ball')
        plt.show()

plot_runs_by_balls()
