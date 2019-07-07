# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#Funtion creation
def plot_deliveries_by_team():
    '''Plot no of deliveres for each team'''
    yaxis=ipl_df['batting_team'].value_counts()
    xaxis = data.index
    plt.bar(xaxis , yaxis, label = 'balls played')
    plt.legend()
    plt.xticks(rotation = '90')
    plt.show()

#Funtion call
plot_deliveries_by_team()






