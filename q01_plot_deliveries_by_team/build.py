# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_deliveries_by_team():
    ipl1=ipl_df.groupby('team1').match_code.agg(['count'])
    ipl1.plot(kind='bar')
plot_deliveries_by_team()


