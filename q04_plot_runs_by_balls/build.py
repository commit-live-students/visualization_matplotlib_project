import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    d = ipl_df.groupby('batsman')

    player_ball_count = d['delivery'].count()
    player_total_runs = d['runs'].sum()

    player_delivery_runs = pd.concat([player_ball_count, player_total_runs], axis=1)
    #print player_delivery_runs
    player_delivery_runs.plot(kind='scatter', x='delivery', y='runs')
    plt.show()


plot_runs_by_balls()
