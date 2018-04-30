# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df=ipl_df[['toss_winner','toss_decision','delivery']][ipl_df['toss_decision']=='bat']
  #  plt.bar(weekly_data.index, weekly_data['Visibility (km)'])
    tmp= ipl_df.groupby(['toss_winner']).agg('count')
    plt.bar(tmp.index,tmp['delivery'])
    plt.xticks(rotation=90)
    plt.show()

plot_deliveries_by_team()

# Solution


