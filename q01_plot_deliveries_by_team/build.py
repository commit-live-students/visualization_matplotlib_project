# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    
    #create figure for drawing data
    fig = plt.figure() 
    
    # group data by batting team and use count as aggregator, then select delivery column since result in the form of pandas
    data = ipl_df.groupby('batting_team').count()['delivery']
    
    # plot bar graph
    plt.bar(data.index, data.values)
    
    # rotate ticks of x axis by 30
    plt.xticks(rotation = 30)
    plt.show()
    
plot_deliveries_by_team()





