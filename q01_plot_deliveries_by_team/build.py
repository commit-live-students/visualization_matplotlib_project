# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    plt.figure()
    plt.bar(ipl_df.index.ipl_df)
    plt.xlabel('batting_team', fontsize=5)
    plt.ylabel('count_of_deli', fontsize=5
    plt.show()
    

plot_deliveries_by_team()


