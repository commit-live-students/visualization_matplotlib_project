# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    batting_team = ipl_df['batting_team']
    deliveries_by_team = batting_team.value_counts()
    x_series = np.arange(len(deliveries_by_team.index))
    plt.bar(x_series, deliveries_by_team)
    plt.xticks(x_series, deliveries_by_team.index.values, rotation=90)
    plt.show()




