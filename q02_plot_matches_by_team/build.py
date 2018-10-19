# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ipl_df1 = ipl_df[['batting_team','match_code']].groupby(['batting_team']).nunique()
    plt.bar(ipl_df1.index, ipl_df1['match_code'])
    plt.title('Matches Played')
    plt.xlabel('Teams')
    plt.ylabel('Match')
    plt.show()
    
plot_matches_by_team()

