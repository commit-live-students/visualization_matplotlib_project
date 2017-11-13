import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    runs_n_balls = ipl_df.groupby('batsman').agg({
    'runs': 'sum',
    'delivery': 'count'})
    plt.scatter(x=runs_n_balls['delivery'],y=runs_n_balls['runs'])
    plt.xlabel('Deliveries')
    plt.ylabel('Runs')
    plt.show()
    print runs_n_balls

#plt.figure(3)
#plot_runs_by_balls()
