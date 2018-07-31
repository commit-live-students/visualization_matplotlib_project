# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    xseries = ipl_df['batting_team']
    yseries = ipl_df['delivery']
    plt.plot(xseries,yseries)
    plt.show()


