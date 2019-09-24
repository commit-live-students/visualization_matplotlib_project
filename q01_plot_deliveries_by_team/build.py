import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    gdf_ipl = ipl_df.groupby('batting_team')
    bat_team_deliveries = gdf_ipl.delivery.count()
    print bat_team_deliveries
    bat_team_deliveries.plot(kind='bar')
    plt.show()
