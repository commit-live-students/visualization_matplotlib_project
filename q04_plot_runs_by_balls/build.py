import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_runs_by_balls():
    delivery=pd.DataFrame({'delivery' : ipl_df.groupby(['match_code','batsman'])['delivery'].count()}).reset_index()
    runs=pd.DataFrame({'runs' : ipl_df.groupby(['match_code','batsman'])['runs'].sum()}).reset_index()
    merge=pd.merge(delivery, runs, how='inner', on=['match_code', 'batsman'])
    plt.scatter(merge['delivery'], merge['runs'])
    plt.show()
