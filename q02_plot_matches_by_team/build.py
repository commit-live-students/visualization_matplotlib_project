# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    matches_by_team = ipl_df[['batting_team', 'match_code']].groupby(['batting_team']).aggregate('nunique')
    x_series = np.arange(len(matches_by_team.index))

    plt.bar(x_series, matches_by_team['match_code'])
    plt.xlabel('Team')
    plt.ylabel('Matches Count')
    
    plt.xticks(x_series, matches_by_team.index.values, rotation=90)
    plt.show()
    print(matches_by_team)
plot_matches_by_team()


