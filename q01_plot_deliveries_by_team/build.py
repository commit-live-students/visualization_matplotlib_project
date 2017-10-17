# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
#print(ipl_df)

def plot_deliveries_by_team():
    s1=ipl_df.groupby('batting_team')['delivery'].agg(['count'])
#     print(ipl_df['batting_team'])
#     plt.bar(x=ipl_df[['batting_team']],y=ipl_df[['batting_team']])
    plt.bar(np.arange(len(s1)),s1.values)
    plt.title('Total no of deliveries played')
    plt.xlabel('team names')
    plt.ylabel('count of deliveries')

    plt.xticks(np.arange(len(s1)),s1.index,rotation=45)

    plt.show()

plot_deliveries_by_team()
