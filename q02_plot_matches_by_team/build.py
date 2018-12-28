# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    team_details = ipl_df.groupby(['batting_team','match_code']).count()
    teams_per_match = team_details.index.values
    teams_details = []
    
    for x in range(0,len(teams_per_match)):
        teams_details.append(teams_per_match[x][0])
    
    values, counts = np.unique(teams_details, return_counts=True)
    x1_series = list(values)
    y1_series = list(counts)
    plt.bar(x1_series,y1_series)
    plt.xticks(x1_series , rotation = 90)
    plt.xlabel('batting_team')
    plt.ylabel('delivery')
    plt.show()


