# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    count=ipl_df.groupby(ipl_df['batting_team']).agg('nunique')
    plt.bar(count.index,count['match_code'])
    plt.title('count of matches/teams')
    plt.xlabel('batting_teams')
    plt.ylabel('count of matches')
    plt.xticks(count.index,rotation=90)
    plt.show()
plot_matches_by_team()
    

