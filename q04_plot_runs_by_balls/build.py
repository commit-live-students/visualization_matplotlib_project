import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():

    ipl_df_balls = ipl_df.groupby(['match_code','batsman'])['runs'].count()
    ipl_df_balls = ipl_df_balls.reset_index(name='balls')

    ipl_df_runs = ipl_df.groupby(['match_code','batsman'])['runs'].sum()
    ipl_df_runs = ipl_df_runs.reset_index(name='runs')

    ipl_df_scorecard = ipl_df_balls.merge(ipl_df_runs,how='inner',left_on = ['match_code','batsman'],right_on = ['match_code','batsman'])


    plt.scatter(ipl_df_scorecard['balls'],ipl_df_scorecard['runs'])
    plt.show()

# Solution
