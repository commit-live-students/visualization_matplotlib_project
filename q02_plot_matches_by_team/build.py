# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ipl_df_grouped = ipl_df.groupby(ipl_df['batting_team']).agg('nunique')['match_code']
    x=ipl_df_grouped.keys()
    y=ipl_df_grouped.values
    sTitle = 'Total number of matches played by each team'
    plt.bar(x,y,label=sTitle)
    plt.xticks(rotation=90)
    plt.show()



