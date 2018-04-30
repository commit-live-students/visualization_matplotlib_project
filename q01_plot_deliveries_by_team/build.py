# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    x_axis = ipl_df['batting_team'].unique()
    y_axis = ipl_df.groupby('batting_team').agg('count')['delivery']
    x_axis.sort()
    # Solution
    plt.xlabel('Batting Team')
    plt.ylabel('Delivery played')
    plt.bar(x_axis,y_axis)
    plt.xticks(rotation=75)
    plt.show()
    
plot_deliveries_by_team()


