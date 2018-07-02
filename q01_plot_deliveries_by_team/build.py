# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    g = ipl_df.groupby(ipl_df['batting_team']).count()
    plt.bar(g.index, g['delivery'])
    plt.xticks(rotation=90)
    plt.show()

plot_deliveries_by_team()
g = ipl_df.groupby(ipl_df['batting_team']).count()
g['delivery']


