# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    match_data = ipl_df.groupby(ipl_df['batting_team']).agg('nunique')
    plt.bar(match_data.index,match_data['match_code'])
    plt.xlabel('Batting Teams')
    plt.ylabel('Matches')
    plt.title('Total Matches Played by Each Team')
    plt.xticks(match_data.index,rotation=45)
    plt.show()

