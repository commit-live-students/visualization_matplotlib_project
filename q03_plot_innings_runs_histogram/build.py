import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    x = ipl_df.groupby(['match_code','inning'] , as_index=False).agg({'delivery':'count','runs':'sum'})
    f, axarr = plt.subplots(2, sharex=True)
    y1 = x['inning'] == 1
    y2=x['inning'] == 2
    y1 = x[y1]
    y2=x[y2]
    i1 = range(0,len(y1.index))
    i2 = range(0,len(y2.index))
    axarr[0].bar(i1,y1['runs'])
    axarr[0].set_title('Sharing X axis')
    axarr[1].bar(i2,y2['runs'])
# Solution
