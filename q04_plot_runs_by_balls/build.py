# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_runs_by_balls():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    print (ipl_df.columns)
    runs= ipl_df.groupby(['match_code','batsman']).agg({'runs':'sum'})
    return ipl_df.head()
    
    
plot_runs_by_balls()
# Solution


