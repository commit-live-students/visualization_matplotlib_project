import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    fig, axes = plt.subplots(nrows=1, ncols=2)
    first = ipl_df[(ipl_df['inning'] == 1)]
    second = ipl_df[(ipl_df['inning'] == 2)]
    axes[0].hist(first['runs'], bins=10)
    axes[1].hist(second['runs'],bins=10)
    plt.show()
