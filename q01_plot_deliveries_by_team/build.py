# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)



def plot_deliveries_by_team():
    #print ipl_df
    df = ipl_df.loc[:, ['batting_team', 'delivery']]
    df['count'] = 1
    individual_values = df.pivot_table('count', aggfunc=np.sum, index='batting_team')
    plots = individual_values.plot(kind='bar')
    plt.show()
    
    

plot_deliveries_by_team()








