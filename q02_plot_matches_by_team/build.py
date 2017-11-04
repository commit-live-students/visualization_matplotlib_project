import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('agg')

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():

    ball_played_df = ipl_df.groupby(['match_code','batsman'],as_index=False).count()['delivery']
    runs_scored_df = ipl_df.groupby(['match_code','batsman'],as_index=False).sum()['runs']
    plt.scatter(ball_played_df,runs_scored_df)
    plt.show()
