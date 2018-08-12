import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    data=ipl_df.groupby(by='delivery')[['runs','delivery']].sum()
    plt.scatter(data.index,data['runs'])
    plt.show()

plot_runs_by_balls()
