import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    a = ipl_df.groupby(by=['match_code','inning'],as_index=0)['runs'].count()
    b = a[a['inning']==1]
    c = a[a['inning']==2]
    plt.subplot(1,2,1)
    b['runs'].hist()
    plt.subplot(1,2,2)
    c['runs'].hist()
plt.show()
