# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    x1= ipl_df.groupby(['match_code','team1'])['team1'].count()
    x2= ipl_df.groupby(['match_code','team2'])['team1'].count()
    x=pd.DataFrame(x1.append(x2))
    y=pd.DataFrame(list(x.index))
    z=y[1].value_counts()
    plt.bar(x=list(z.index),height=z)
    plt.show()

# Solution

plot_matches_by_team()



