# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    a=ipl_df.groupby(ipl_df['batting_team']).agg('count')['delivery']
    x=a.keys()
    y=a.values
    plt.xticks(rotation=90)
    sTitle = 'Total number of deliveries played by each team'
    plt.bar(x,y,label=sTitle)
    plt.show()
    return





