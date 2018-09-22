# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    valuereqd=ipl_df.groupby('batting_team')['delivery'].nunique()
    valuereqd1=ipl_df['batting_team'].unique()
    plt.bar(valuereqd1,valuereqd)
    plt.show()

plot_deliveries_by_team()


