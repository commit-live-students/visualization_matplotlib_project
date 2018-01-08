import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    testscatter = ipl_df.groupby('batsman').agg({'runs': 'sum','delivery' : 'nunique'})
    xvalue = testscatter['runs']
    yvalue = testscatter['delivery']
    plt.scatter(xvalue,yvalue)
    plt.title('Scatter plot for balls Vs runs')
    plt.xlabel('runs')
    plt.ylabel('delivery')
    plt.show()

# Solution
