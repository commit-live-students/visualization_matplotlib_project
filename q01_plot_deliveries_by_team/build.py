# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    x=pd.DataFrame(ipl_df.groupby(['batting_team'])['delivery'].count())
    plt.bar(x=list(x.index),height=x.delivery)
    plt.show()
    


# Solution



