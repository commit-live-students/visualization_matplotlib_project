# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    delv = (ipl_df.groupby(by=('batting_team') )).count()

    delv['delivery'].plot.bar()
    return plt.show()

plot_matches_by_team()
# Solution


