# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df= ipl_df.groupby('batting_team')['match_code'].nunique().reset_index()
    x=df['batting_team']
    y=df['match_code']
    
    plt.bar(x,y)
    plt.title('Matches Played By Each Team')
    plt.ylabel('Batting Teams')
    plt.xlabel('Matches Played')
    plt.show()
      
plot_matches_by_team()




