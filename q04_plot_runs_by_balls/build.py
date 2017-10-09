# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs = ipl_df.groupby(ipl_df.batsman).sum()
    balls = ipl_df.groupby(ipl_df.batsman).count()
    plt.scatter(balls['match_code'],runs['runs'])
    plt.show()
