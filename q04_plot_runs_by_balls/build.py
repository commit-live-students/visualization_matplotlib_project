# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    df1 = ipl_df.groupby('batsman').agg({'runs':np.sum})
    df2 = ipl_df.groupby('batsman').count()
    df2 = df2.rename(index=str, columns={'match_code': 'balls_played'})
    df2 = df2[['balls_played']]
    df1 = df1.join(df2)
    ax2 = df1.plot.scatter(x='balls_played',y='runs')





