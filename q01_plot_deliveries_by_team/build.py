# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    rows_for_batting = ipl_df.loc[ipl_df['toss_decision']=='bat']
    data_for_graph = rows_for_batting['toss_winner'].value_counts()
    plt.bar(data_for_graph.index, data_for_graph.values)
# Solution



