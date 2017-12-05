import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    teams=ipl_df[['batting_team','delivery']]
    g_teams=teams.groupby('batting_team')
    g_teams.count().plot(kind='bar')
    plt.show()
