import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    data = ipl_df.groupby(['match_code','inning'])['runs'].agg('sum')
    inning1 = data[:,1]
    inning2 = data[:,2]
    plt.subplot(1,2,1)
    plt.hist(inning1)
    plt.subplot(1,2,2)
    plt.hist(inning2)
    plt.show()
