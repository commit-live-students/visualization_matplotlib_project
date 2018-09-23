# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')


# Solution
def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df.groupby('batting_team').match_code.agg('nunique').plot(kind='bar',title='Batting team vs Unique/distinct count of matches')
    plt.xlabel('Teams',size = 15)
    plt.xticks(rotation= 90,ha='right')
    plt.ylabel('Unique counts of matches',size = 15)
    plt.show()
    
plot_matches_by_team()






