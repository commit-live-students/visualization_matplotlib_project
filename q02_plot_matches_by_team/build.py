import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    teams=ipl_df[['batting_team']]
    g_teams=teams.groupby('batting_team')
    g_teams[['batting_team']].count().plot(kind='bar')
    plt.show()
