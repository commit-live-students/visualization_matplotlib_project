# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
#     iplData = ipl_df.groupby(['batsman']).agg({'delivery':'count', 'runs': 'sum'})
#     print(iplData)
    iplData = ipl_df.groupby(['match_code','batsman']).agg({'delivery':'count', 'runs': 'sum'})
#     print(iplData)
    plt.scatter(iplData['delivery'], iplData['runs'],c='b')
    plt.show()
    
    
plot_runs_by_balls()


