# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    bar_plot = ipl_df.groupby(['team1'])['delivery'].count().plot.bar()
    bar_plot.set_xlabel('teams')
    bar_plot.set_ylabel('counts of deliveries')
    
    return


