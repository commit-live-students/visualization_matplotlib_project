# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_deliveries_by_team():
    all_teams = ipl_df['batting_team']
    x_series = pd.Series(all_teams.value_counts().index)
    y_series = pd.Series(all_teams.value_counts().values)

    plt.bar(x_series,y_series)
    plt.xticks(rotation = 45)
    plt.title('graph')
    plt.xlabel('batting_team')
    plt.ylabel('delivery')
    plt.show()

