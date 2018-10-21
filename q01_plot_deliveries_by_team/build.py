# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    x = ipl_df['batting_team']
    #y = ipl_df.groupby('batting_team')['delivery'].count()
    y = ipl_df['delivery']
    print(x.shape,y.shape)
    #plt.scatter(x,y)
    plt.plot(x,y)
    plt.show()

#plot_deliveries_by_team()


# Solution



