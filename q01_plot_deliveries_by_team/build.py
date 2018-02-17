import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    data = ipl_df.pivot_table(values='delivery',index=['batting_team'],aggfunc='count')
    data.plot(kind='bar')
    plt.title('Deliveries faced by Teams Graph')
    plt.xlabel('Teams')
    plt.ylabel('No. of Deliveries')
    plt.show()
