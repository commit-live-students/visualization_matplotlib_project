# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    ipl_df['team1'].value_counts().plot(kind='bar')
    plt.show()

plot_deliveries_by_team()


