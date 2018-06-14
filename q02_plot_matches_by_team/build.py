# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    new_df=ipl_df.groupby('batting_team').nunique()
    plt.bar(new_df.index,new_df['match_code'])
    plt.xticks(rotation=90)
    plt.title('total number of matches played by each team')
    plt.xlabel('batting teams')
    plt.ylabel('unique/distinct count of matches')
    plt.show()


