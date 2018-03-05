import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    teams_x=pd.unique(ipl_df['batting_team'])
    match_y=ipl_df.groupby(['batting_team'])['match_code'].nunique()
    plt.xlabel('Team Names')
    plt.ylabel('No.Of Matches Played')
    plt.bar(teams_x,match_y)
    plt.xticks(teams_x,rotation='vertical')
    plt.show()
