# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_matches_by_team():
    batting_team = ipl_df['batting_team']
    matches_count = batting_team.value_counts()
    x_series = np.arange(len(matches_count.index))
    plt.bar(x_series, matches_count)
    plt.xticks(x_series, matches_count.index.values, rotation=90)
    plt.show()


plot_matches_by_team()







