import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    match_team=ipl_df[['match_code','batting_team']]
    by_team=match_team.groupby('batting_team').nunique()
    #print(by_team)
    by_team.plot(kind='bar')
    plt.xlabel('batting_team')
    plt.ylabel('counts of matches played')
    plt.show()
