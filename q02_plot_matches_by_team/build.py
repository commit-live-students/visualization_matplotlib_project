# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    batting_team = ipl_df['batting_team']
    b= ipl_df['batting_team'].unique()
    plt.bar(batting_team,b)
b= ipl_df.groupby(ipl_df['batting_team']).agg({'batting_team':pd.Series.nunique})#.unique()
b


