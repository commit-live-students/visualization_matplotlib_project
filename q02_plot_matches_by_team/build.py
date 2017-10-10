# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    balls_data = ipl_df.groupby(ipl_df.batting_team).agg('nunique')
    n = len(balls_data['match_code'])
    teams = np.arange(1, int(n+1))
    plt.bar(teams, balls_data['match_code'])

    plt.title('Visibility by week, 2012')
    plt.xlabel('Day of week')
    plt.ylabel('Visibility (km)')

    plt.xticks(teams,balls_data.index,rotation=90)
    plt.show()
