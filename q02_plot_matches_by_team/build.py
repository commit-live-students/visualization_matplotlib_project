# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    y=ipl_df.groupby('batting_team')['match_code'].nunique()
    x=np.arange(0,13)
    plt.bar(x,y)
    plt.xticks(x,np.unique(ipl_df.iloc[:,13]),rotation=90)

    plt.show()

    # Solution
#plot_matches_by_team()
