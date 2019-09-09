import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_run_histogram():
    a = ipl_df[['match_code','inning','delivery']]
    b = ipl_df[['match_code','inning','runs']]
    c = a.groupby(as_index=False,by=('match_code','inning')).count()
    d = b.groupby(as_index=False,by=('match_code','inning')).sum()
    e = c.merge(d)
    inning1 = e[e['inning']==1]
    inning2 = e[e['inning']==2]
    inning1[['match_code','delivery','run']].plot(kind='hist')
    plt.show()
    inning2[['match_code','delivery','run']].plot(kind='hist')
    plt.show()
# Solution
