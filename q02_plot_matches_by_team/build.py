# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    a=ipl_df.groupby(['batting_team'])['match_code'].agg('nunique')
    plt.title('plot_mactches_by_team')
    plt.xlabel('batting_team')
    plt.ylabel('matches_played')
    p=np.arange(len(a))
    plt.bar(p,a.values)
    plt.xticks(p,a.index)
    plt.show()
