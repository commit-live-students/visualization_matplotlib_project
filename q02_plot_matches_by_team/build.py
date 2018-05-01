# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    iplGroupBy = ipl_df.groupby(ipl_df['batting_team']).nunique()
    plt.bar(iplGroupBy.index,iplGroupBy['match_code'])
    plt.title('Number of matches played')
    plt.xlabel('Team')
    plt.ylabel('Number of matches')

    plt.xticks(iplGroupBy.index, rotation=90)
    plt.plot()
    #return iplGroupBy

plot_matches_by_team()

