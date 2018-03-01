import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():

    runs_scored = pd.pivot_table(ipl_df, values='total', index=['match_code', 'batsman','inning'], \
                      aggfunc=np.sum)
    balls_played = pd.pivot_table(ipl_df, values='delivery', index=['match_code', 'batsman','inning'], \
                      aggfunc= len)

    plt.scatter(runs_scored,balls_played)
    plt.show()
