# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    
    c=ipl_df.groupby('batting_team').agg({'delivery':'count'}).reset_index()
    c.plot(kind='bar')
    plt.xticks(index,list(c['batting_team']))
    plt.xlabel('Batting team')
    plt.ylabel('Deliveries')
    plt.show()


c=ipl_df.groupby('batting_team').agg({'delivery':'count'}).reset_index()
c['delivery']
type(c)
c.iloc[:,0]

c=c.reset_index()
c.iloc[:,0]
ax=c[['batting_team','delivery']].plot(kind='bar')
plt.show()
ax
ax=c[['batting_team','delivery']].plot(kind='bar')
ax
plt.show()
ax


