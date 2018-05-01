# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    
    iplGroupBy = ipl_df.groupby(['match_code','batsman']).agg({'delivery':'count', 'runs': 'sum'})
    plt.scatter(iplGroupBy['delivery'], iplGroupBy['runs'],c='r')
    plt.plot()
    #return iplGroupBy.reset_index()
    #return ipl_df.columns.values
plot_runs_by_balls()

