#%load q01_plot_deliveries_by_team/build.py

import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt

ipl_df=pd.read_csv('./data/ipl_dataset.csv')

# gr=ipl_df.groupby('batting_team').delivery.agg('count')

# plt.bar(gr.index,gr,title='Bar graph of \n Batting team vs count of deliveries ')
# plt.show()
def plot_deliveries_by_team():
    ipl_df.groupby('batting_team').delivery.agg('count').plot(kind='bar',title='Batting team vs count of deliveries ')
    plt.xlabel=('batsman')
    plt.ylabel=('runs')
    plt.show() 
    
plot_deliveries_by_team()




