import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    deliveries_data = ipl_df.groupby(ipl_df.batting_team).sum()
    #print deliveries_data
    #print list(deliveries_data['inning'])
    #print deliveries_data.index
    #plt.bar(deliveries_data.index,list(deliveries_data['runs']))
    plt.title('Total deliveries faced')
    plt.xlabel('Team name')
    plt.ylabel('No. of deliveries')
    plt.show()
