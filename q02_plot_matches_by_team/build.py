# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution

def plot_matches_by_team():
    x=ipl_df.groupby('batting_team').nunique()
    plt.bar(x.index,x['match_code'])
    plt.xticks(rotation=90)
    plt.title('Matches played bar graph')
    plt.xlabel('Team name')
    plt.ylabel('Number of matches')
    plt.show()
    
#plot_matches_by_team()

