# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    table = ipl_df.groupby(['match_code','inning'])['total'].sum()
    firstInnings = table[:,1]
    secondInnings = table[:,2]
    hist, axes = plt.subplots(1,2)
    axes[0].hist(firstInnings.values)
    axes[1].hist(secondInnings.values)
    return
    
plot_innings_runs_histogram()


