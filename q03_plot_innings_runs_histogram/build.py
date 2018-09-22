# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    df=ipl_df[['inning','runs']] #creating the require df fr
    df.groupby('inning')['inning'].sum().plot(kind='hist')
    plt.show()


