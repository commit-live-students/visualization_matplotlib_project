# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    ball_count = ipl_df[['match_code','batsman','delivery']].groupby(['match_code','batsman'])['delivery'].count()
    runs = ipl_df[['match_code','batsman','runs']].groupby(['match_code','batsman'])['runs'].sum()
    ball_count = pd.DataFrame(ball_count, columns = ['match_code','batsman','delivery'])
    runs = pd.DataFrame(runs, columns = ['match_code','batsman','runs'])
    #print(runs)
    merged = pd.merge(ball_count,runs, left_on= 'match_code', right_on= 'match_code')
    x = merged['delivery']
    y = merged['runs']
    plt.figure()
    plt.subplot(111)
    plt.scatter(x,y)
    
    
plot_runs_by_balls()


