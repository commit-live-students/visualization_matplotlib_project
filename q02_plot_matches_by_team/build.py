# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
# Solution
def plot_matches_by_team():
    x_axis =np.sort(ipl_df['batting_team'].unique())
    y_axis = ipl_df.groupby('batting_team')['match_code'].nunique()
    plt.bar(x_axis,y_axis)
    plt.xlabel('Teams')
    plt.ylabel('Number of matches')
    plt.xticks(rotation=75)
    plt.show()
    
plot_matches_by_team()

