# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    balls_played_by_player = ipl_df.groupby(['match_code','batsman'])['delivery'].agg('count')
    runs_made_by_player = ipl_df.groupby(['match_code','batsman'])['runs'].agg('sum')
    plt.scatter(balls_played_by_player, runs_made_by_player)
    
    return
plot_runs_by_balls()


