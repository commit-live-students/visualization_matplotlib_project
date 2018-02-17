import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    ns = ipl_df.groupby(by='delivery')[['runs','delivery']].sum()
    plt.scatter(ns.index,ns['runs'])
    plt.show()
