# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    ipl_df1 = ipl_df[['batting_team','delivery']].groupby(['batting_team']).count()
    plt.bar(ipl_df1.index, ipl_df1['delivery'])
    plt.title('Deliveries Played')
    plt.xlabel('Teams')
    plt.ylabel('Deliveries')
    plt.show()
    
plot_deliveries_by_team()

