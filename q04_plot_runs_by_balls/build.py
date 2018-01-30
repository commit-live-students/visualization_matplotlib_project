import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_runs_by_balls():
    y = ipl_df.groupby(['batsman'])['runs'].sum()
    y1 = ipl_df.groupby(['batsman'])['delivery'].count()

    plt.scatter(y1,y)
    plt.xlabel('No. of balls played')
    plt.ylabel('No. of runs')
    plt.title('Relation between run made and balls played')
    plt.show()

# Solution
