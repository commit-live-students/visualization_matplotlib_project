# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    x=ipl_df.groupby('batting_team')['delivery'].count()
    plt.bar(np.arange(13),x)
    plt.xticks(np.arange(13),x.index)
    plt.show()


plot_deliveries_by_team()   
