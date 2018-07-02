# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df_tmp=ipl_df[['match_code','batting_team']]
    tmp= ipl_df_tmp.groupby(['batting_team']).agg({'match_code':pd.Series.nunique})
    plt.bar(tmp.index,tmp['match_code'])
    plt.xticks(rotation=90)
    plt.show()

plot_matches_by_team()

# Solution


