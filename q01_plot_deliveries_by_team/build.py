# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    df= DataFrame(ipl_df[['batting_team','delivery']].groupby(['batting_team'])['delivery'].count())
    df.columns=['deliveries']
    df.index.name=['batting_team']
    df.plot(kind='bar')
    plt.show()
    return plt.show()
