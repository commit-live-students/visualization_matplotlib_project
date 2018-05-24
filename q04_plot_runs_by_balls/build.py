# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    new_data=ipl_df.groupby(['match_code','batsman']).agg({'delivery':'count', 'runs':'sum'})
    x=new_data['delivery']
    y=new_data['runs']
    plt.figure(figsize=(30,30))
    plt.xlabel('no of balls')
    plt.ylabel('no of runs')
    plt.title('performance of players')
    plt.scatter(x, y, c='b')
    plt.show()
    


