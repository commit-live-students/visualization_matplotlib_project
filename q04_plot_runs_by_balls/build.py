import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    table = ipl_df.pivot_table(index ='delivery', values=['runs'], aggfunc = np.sum)
    plt.scatter(table.index,table['runs'])
    plt.show()

# Solution
