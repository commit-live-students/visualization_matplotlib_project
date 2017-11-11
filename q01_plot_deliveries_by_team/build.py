# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    #df = ipl_df[basestring]
    Y = ipl_df.groupby(['batting_team'])['delivery'].count()
    Y.plot.bar()
    plt.show()

# Solution
