# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    my_range = len(ipl_df.groupby('batting_team')['delivery'].count())
    my_counts = ipl_df.groupby('batting_team')['delivery'].count()
    plt.bar(np.arange(my_range),my_counts)
    plt.xticks(np.arange(my_range),list((my_counts).keys()),rotation=90)








