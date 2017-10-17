# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():

    s1=ipl_df.groupby('batting_team')['match_code'].agg(['count'])
    #print(s1)
    plt.title('Total no of matches played')
    plt.xlabel('team names')
    plt.ylabel('count of matches')
    plt.bar(np.arange(len(s1)),s1.values)
    plt.xticks(np.arange(len(s1)),s1.index,rotation=45)

    plt.show()

plot_matches_by_team()
