# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')


def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    ipl_df.groupby('batting_team')['batting_team'].count().plot(kind='bar')
    plt.show()
     




