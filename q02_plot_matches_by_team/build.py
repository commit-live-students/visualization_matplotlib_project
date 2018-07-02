# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    g = ipl_df.groupby(ipl_df['batting_team']).agg('nunique')
    data = g['match_code']
    plt.bar(data.index, data.values)
    plt.xticks(rotation=90)
    plt.show()
plot_matches_by_team()


