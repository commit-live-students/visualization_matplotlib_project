import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_deliveries_by_team():
    x = ipl_df.groupby(ipl_df.batting_team).agg('count')
    index = x.index
    i = range(0,len(index))
    y = x['delivery']
    plt.bar(i, y.values)
    plt.xticks(i,index,rotation=90)
    plt.show()
