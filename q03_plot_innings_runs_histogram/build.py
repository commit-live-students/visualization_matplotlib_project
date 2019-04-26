import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():
    d2 = ipl_df.groupby(['inning','match_code']).agg('runs').sum()
    plt.figure(1)
    plt.subplot(121)
    plt.plot(d2[1])
    plt.subplot(122)
    plt.plot(d2[2])
    plt.show()

plot_innings_runs_histogram()
