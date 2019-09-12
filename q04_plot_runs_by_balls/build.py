import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1 = pd.DataFrame(ipl_df.groupby(['match_code','batsman'])['delivery'].count())
    df2 = pd.DataFrame(ipl_df.groupby(['match_code','batsman'])['runs'].sum())
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    df_plot = df.plot(kind='scatter', x='delivery', y='runs')

    return df_plot
#print plot_runs_by_balls()
plt.show()
