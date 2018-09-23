# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Solution
def plot_runs_by_balls():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    
    runs = pd.DataFrame(ipl_df.groupby('batsman').runs.agg('sum'))
    deliveries = pd.DataFrame(ipl_df.groupby('batsman').delivery.agg('count'))
    
    V = runs.merge(deliveries, how='inner',left_index=True,right_index=True)
    
    plt.scatter(V.runs,V.delivery)
    plt.xlabel('Runs',size=15)
    plt.ylabel('Deliveries',size=15)
    plt.show()
    
plot_runs_by_balls()    


