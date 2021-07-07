# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    group= ipl_df.groupby('batting_team').agg('nunique')
    series= group['match_code']
    plt.xlabel('Batting Team')
    plt.ylabel('Number of Matches Played')
    plt.bar(series.index,series)
    plt.show()



