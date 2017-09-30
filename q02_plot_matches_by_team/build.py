import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl = pd.read_csv('data/ipl_dataset.csv', index_col=0)


def plot_matches_by_team():
    matches_by_team = ipl_df[['batting_team', 'match_code']].groupby(['batting_team']).aggregate('nunique')
    x_series = np.arange(len(matches_by_team.index))

    plt.bar(x_series, matches_by_team['match_code'])
    plt.xlabel('Team')
    plt.ylabel('Matches Count')
    
    plt.xticks(x_series, matches_by_team.index.values, rotation=90)
    plt.show()

plot_matches_by_team()