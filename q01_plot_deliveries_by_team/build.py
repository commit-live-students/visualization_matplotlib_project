# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_deliveries_by_team():
    ipl_data = ipl_df.groupby(ipl_df['batting_team']).sum()
    plt.bar(ipl_data.index,ipl_data['delivery'])
    plt.xlabel('Batting Teams')
    plt.ylabel('Deliveries')
    plt.title('IPL Team Data')
    plt.xticks(ipl_data.index, rotation=45)
    plt.show()

