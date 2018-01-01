# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df= DataFrame(ipl_df[['batting_team','match_code']].groupby(['batting_team'])['match_code'].nunique())
    df.columns=['match_code']
    df.index.name=['batting_team']
    df.plot(kind='bar')
    plt.show()
    return plt.show()
print plot_matches_by_team()
