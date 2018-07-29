# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():
    table=ipl_df(['match_code','innings'])['total'].sum()
    first_inn=table[:,1]
    second_inn=table[:,2]
    axes[0].hist(first_inn.values)
    axes[1].hist(second_inn.values)
    return
    

# Solution



