import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
from collections import Counter
def plot_matches_by_team():
    team_list = []
    for i in (ipl_df['match_code'].value_counts().index):
        team_list.append(((ipl_df.loc[ipl_df['match_code'] == i, ['team1','team2']]).iloc[0])[0])
        team_list.append(((ipl_df.loc[ipl_df['match_code'] == i, ['team1','team2']]).iloc[0])[1])
    teams = list(Counter(team_list).keys())
    total_matches = list(Counter(team_list).values())
    plt.bar(range(len(Counter(team_list))),total_matches,tick_label=teams)
    plt.show()
