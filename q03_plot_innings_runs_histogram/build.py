import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df=ipl_df[['match_code','inning','total']]
    df2=df.groupby(['match_code','inning']).sum()
    inn1=new_df[new_df.index.get_level_values('inning')==1]
    inn2=new_df[new_df.index.get_level_values('inning')==2]
    plt.subplot(1,2,1)
    plt.hist(inn1.values)
    plt.subplot(1,2,2)
    plt.hist(inn2.values)
    plt.show()
