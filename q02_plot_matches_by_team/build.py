# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    uniqueteams = ipl_df['batting_team'].unique()
    x = np.arange(len(uniqueteams))
    y = ipl_df.groupby(['batting_team'])['match_code'].agg('nunique')
    #print(y)

    plt.bar(x, y)

    #plt.title('')
    plt.xlabel('Batting teams')
    plt.ylabel('Matches played')

    plt.xticks(x, uniqueteams, rotation=90)

    plt.show()


#print(ipl_df)
# Solution
