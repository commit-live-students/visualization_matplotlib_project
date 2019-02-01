# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    a=ipl_df.groupby('batting_team').agg({'delivery':'count'}).reset_index()
    a.plot(kind='bar')
    plt.xticks(index,list(a['batting_team']))
    plt.xlabel('Batting team')
    plt.ylabel('Deliveries')
    plt.show()
    
    a=ipl_df.groupby('batting_team').agg({'delivery':'count'}).reset_index()
    a['delivery']
    type(a)
    a.iloc[:,0]
    
    a=a.reset_index()
    a.iloc[:,0]
    x=a[['batting_team','delivery']].plot(kind='bar')
    plt.show()
    x
    x=a[['batting_team','delivery']].plot(kind='bar')
    x
    plt.show()
    x


