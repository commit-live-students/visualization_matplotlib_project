# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)



# Solution
def plot_runs_by_balls():
    group1 = ipl_df.groupby([ipl_df['match_code'],ipl_df['batsman']]).agg('count')['delivery']
    group2 = ipl_df.groupby([ipl_df['match_code'],ipl_df['batsman']]).agg('sum')['runs']
    df1 = group1.to_frame()
    df2 = group2.to_frame()
    df_1 = df1.reset_index()
    df_2 = df2.reset_index()
    new_group = pd.merge(df_1,df_2,how='inner',on=['match_code','batsman'])
    y1 = new_group['delivery']
    y2 = new_group['runs']
    plt.scatter(y2,y1)
    plt.show()
    return



