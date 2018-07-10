# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    data = ipl_df.groupby(ipl_df['batting_team'])
    x = data['delivery'].count()
    y = data['runs'].sum()
    axs[0].hist(x)
    axs[1].hist(y)
    

