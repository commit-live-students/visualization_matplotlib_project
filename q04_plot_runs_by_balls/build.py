# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    df1 = ipl_df.groupby('batsman')['runs'].sum()
    df2 = ipl_df.groupby('batsman')['delivery'].count()
    plt.scatter(df2,df1)
    plt.show()
    
# Solution
plot_runs_by_balls()



