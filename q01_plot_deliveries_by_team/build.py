# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
ipl_df.head(2)
#print(ipl_df['batting_team'])
# Solution
def plot_deliveries_by_team():
    iplGroupBy = ipl_df.groupby('batting_team').sum()
    plt.bar(iplGroupBy.index,iplGroupBy['delivery'])
    
    plt.title('Delivery faced by Team')
    plt.xlabel('Team Name')
    plt.ylabel('Number of Deliveries')

    plt.xticks(iplGroupBy.index,  rotation=90)

    plt.show()
    #return iplGroupBy
plot_deliveries_by_team()

