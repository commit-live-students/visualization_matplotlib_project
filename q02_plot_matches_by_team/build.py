# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    team_data = ipl_df.groupby('batting_team')['match_code'].nunique()
    plt.bar(team_data.index,team_data)
    plt.xticks(rotation='90')
    plt.plot()
    plt.show()

plot_matches_by_team()

