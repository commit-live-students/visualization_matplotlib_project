# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    
    runs_per_batsman = ipl_df.groupby(['batsman'])['runs'].sum()
    
    deliveries_faced_per_batsman = ipl_df.groupby(['batsman'])['delivery'].count()
    
    unique_match_per_player = ipl_df.groupby(['batsman'])['match_code'].unique()
    
    unique_match_counts = []
    
    for i in range(len(unique_match_per_player)):
        unique_match_counts.append( len(unique_match_per_player[i]))
    
    avg = []
    
    for i in range(len(unique_match_per_player)):
        avg.append(runs_per_batsman[i]/(deliveries_faced_per_batsman[i]))
    
    plt.scatter(avg,unique_match_counts)
    
    plt.show()










