import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl = pd.read_csv('data/ipl_dataset.csv', index_col=0)


def plot_deliveries_by_team():
    batting_team = ipl_df['batting_team']
    deliveries_by_team = batting_team.value_counts()
    x_series = np.arange(len(deliveries_by_team.index))
    plt.bar(x_series, deliveries_by_team)
    plt.xticks(x_series, deliveries_by_team.index.values, rotation=90)
    plt.show()


plot_deliveries_by_team()
