# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    df = ipl_df[['batting_team','match_code']].groupby('batting_team').agg('count')
    plt.plot(df.index,df.values)
    plt.show()

# Solution
plot_matches_by_team()








