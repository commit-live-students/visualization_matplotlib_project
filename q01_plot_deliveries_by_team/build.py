import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    deliveries= ipl_df.groupby(by=['batting_team'])['delivery'].count()

    team = deliveries.index.tolist()
    team_length = range(len(team))
    deliveries_lst = deliveries.tolist()

    plt.bar(team_length, deliveries_lst)
    plt.xticks(team_length, team, rotation=90)
    plt.show()
