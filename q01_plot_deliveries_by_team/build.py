import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_deliveries_by_team():

    # Get batting team column
    batting_team = ipl_df.iloc[:,13]
    # Count occurences of all the teams in batting team column, which will be
    # equal to no. of deliveries played by that team
    batting_team_deliveries = batting_team.value_counts()
    batting_team_deliveries.plot(kind = 'bar')
    plt.show()
