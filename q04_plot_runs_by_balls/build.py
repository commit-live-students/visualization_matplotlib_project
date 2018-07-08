# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    ballsPlayed = ipl_df.groupby(['match_code','batsman'])['delivery'].count()
    runsMade = ipl_df.groupby(['match_code','batsman'])['total'].sum()
    table = pd.concat([ballsPlayed,runsMade],axis=1)
    print(table.values.transpose())
    x = table.values.transpose()[0]
    y = table.values.transpose()[1]
    #print(table.values.transpose()[0])
    #print(ipl_df.groupby(['batsman'])[])
    plt.scatter(x,y)
    #plt.show()


