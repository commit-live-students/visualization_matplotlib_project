import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    df=ipl_df[['match_code','inning','total']]
    new_df=df.groupby(['match_code','inning']).sum()
    inning1=new_df[new_df.index.get_level_values('inning')==1]
    inning2=new_df[new_df.index.get_level_values('inning')==2]
    plt.subplot(1,2,1)
    plt.hist(inning1.values)
    plt.subplot(1,2,2)
    plt.hist(inning2.values)
    plt.show()
# Solution
