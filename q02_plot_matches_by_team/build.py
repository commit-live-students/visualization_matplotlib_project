# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ipl_df = ipl_df.groupby('batting_team').agg.nunique
    battingteam = ipl_df.set('batting_team')
    plt.bar(battingteam, ipl_df)
    plt.show()

