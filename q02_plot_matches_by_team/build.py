# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    match_count_per_teams=ipl_df[['batting_team','match_code']].groupby('batting_team').aggregate('nunique')
    Series_of_matches=np.arange(len(match_count_per_teams.index))
    plt.bar('bbatting_team',match_count_per_teams['match_code'])
plot_matches_by_team()


