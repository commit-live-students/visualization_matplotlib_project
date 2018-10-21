# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    
    newData = ipl_df.groupby(['match_code', 'inning']).agg('sum')
    x = newData['runs'].values
    num_bins = 50
    
    plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
    
plot_innings_runs_histogram()


