# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    uniqueteams = ipl_df['batting_team'].unique()

    uniqueteams,y = np.unique(ipl_df['batting_team'], return_counts=True)
    x = np.arange(len(uniqueteams))

    plt.bar(x,y)
    plt.xlabel('Batting team')
    plt.ylabel('Deliveries')

    plt.xticks(x, uniqueteams, rotation=90)
    plt.show()



    
