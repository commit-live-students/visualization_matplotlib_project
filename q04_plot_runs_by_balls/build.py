# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    data = ipl_df[['batsman','runs']]
    runs_scored = data.groupby(['batsman'])['runs'].sum()
    balls_played = data.groupby(['batsman'])['runs'].count()
    plt.scatter(balls_played,runs_scored)
plot_runs_by_balls()



