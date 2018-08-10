# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    %matplotlib inline
    batting_team_code = ipl_df[['batting_team','match_code']]
    batting_team_code = batting_team_code.groupby(['batting_team'])['match_code'].nunique().plot(kind='bar', title='Team v/s Match Count')
    
    #plt.bar(batting_team_code)
    #plt.show()
    
plot_matches_by_team()

