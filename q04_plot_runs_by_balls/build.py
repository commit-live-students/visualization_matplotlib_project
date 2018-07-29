# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_runs_by_balls():
    data = ipl_df[['batsman','runs']]
    run_scored = data.groupby(['batsman'])['runs'].sum()
    ball_del = data.groupby(['batsman'])['runs'].count()
    plt.scatter(ball_del,run_scored)
    return


plot_runs_by_balls()



