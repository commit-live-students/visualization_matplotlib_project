# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_deliveries_by_team():
    a = ipl_df.groupby(ipl_df['batting_team'])['delivery'].count()
    y=a.values
    x=a.index
    p=np.arange(int(len(a.index)))
    plt.xticks(p,x)
    plt.bar(p,y)
    plt.title('plot_deliveries_by_team')
    plt.xlabel('Batting Team')
    plt.ylabel('Deliveries')
    plt.show()
