# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
#type(ipl_df)

#a=ipl_df.iloc[0,:]
#a
def plot_deliveries_by_team():
    y=ipl_df.groupby('batting_team')['delivery'].count()
    x=np.arange(0,13)
    #print(y)
    #print(x)

    plt.bar(x,y)
    plt.xticks(x,np.unique(ipl_df.iloc[:,13]),rotation=90)
    plt.show()
    #plt.bar(uni,)
#plot_deliveries_by_team()
