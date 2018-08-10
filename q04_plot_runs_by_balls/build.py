# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1=ipl_df.groupby(['match_code','batsman']).agg('count')['delivery'].to_frame('delivery')
    df2=ipl_df.groupby(['match_code','batsman']).agg(sum)['runs'].to_frame('runs')
    result = pd.concat([df1, df2], axis=1)
    result.plot(x='delivery', y='runs', style='o')



