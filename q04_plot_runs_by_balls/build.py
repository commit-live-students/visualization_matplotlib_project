# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    total_balls=ipl_df[['batsman','delivery']].groupby(['batsman']).count().reset_index()
    total_runs=ipl_df[['batsman','runs']].groupby(['batsman']).sum().reset_index()
    
    df=pd.merge(total_balls,total_runs,on=['batsman'])
    
    plt.scatter(df['delivery'],df['runs'])
    
    
plot_runs_by_balls()



