# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    teams=set(ipl_df['team1'].unique()).union(set(ipl_df['team2'].unique()))
    D=dict(zip(teams,map(len,[[x  for y in ipl_df['batting_team'] if x==y] for x in teams])))
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()




