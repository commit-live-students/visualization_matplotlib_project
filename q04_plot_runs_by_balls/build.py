# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_runs():
    # number of balls played by players
    no_of_balls = ipl_df.groupby('batsman').count()['delivery']
    # total runs made by players
    runs = ipl_df.groupby('batsman', sort = True).sum()['runs']
    #creating figure for plotting data
    fig = plt.figure()
    #using scatter function to show relationship between no of balls and runs
    plt.scatter(no_of_balls, runs)
    
    plt.xlabel('balls playesd')
    plt.ylabel('runs scored')
    
    plt.show()
plot_runs_by_runs()






