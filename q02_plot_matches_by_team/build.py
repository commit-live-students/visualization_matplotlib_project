# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
#     data =ipl_df.groupby(['batting_team']).nunique()['match_code']
    team = ipl_df.groupby(ipl_df['batting_team']).nunique()
#     return team
    plt.bar(team.index,team['match_code'])
    plt.show()

plot_matches_by_team()

