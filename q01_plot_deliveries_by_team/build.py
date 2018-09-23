# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')


# Solution
def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df.groupby('batting_team').delivery.agg('count').plot(kind='bar',title='Bar graph of \n Batting team vs count of deliveries ')
    plt.xlabel('Batting Teams',size = 15)
    plt.ylabel('Count of deliveries', size = 15)
    plt.show()    
    
plot_deliveries_by_team()

   


