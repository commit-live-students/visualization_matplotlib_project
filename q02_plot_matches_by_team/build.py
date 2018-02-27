import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
#print ipl_df.head(0)


def plot_matches_by_team():
    batting_team=ipl_df['batting_team']
    #To group the teams and get their distinct counts
    count_matches_played=ipl_df.groupby(by=['batting_team'])['batting_team'].nunique
    x_series=batting_team
    y_series=count_matches_played

    plt.bar(x_series,y_series)
    plt.title("Total number of matches played by each team")
    plt.xlabel("Batting team")
    plt.ylabel("Count of Matches Played")
    plt.show();
plot_matches_by_team()
