import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df1 = pd.DataFrame(ipl_df.groupby(['match_code', 'batsman', 'inning'])['delivery'].count())
    df2 = pd.DataFrame(ipl_df.groupby(['match_code', 'batsman', 'inning'])['runs'].sum())
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    inning_1 = df.iloc[df.index.get_level_values('inning') == 1]
    inning_2 = df.iloc[df.index.get_level_values('inning') == 2]
    plt.subplot(1,2,1)
    plt.histogram(inning_1, x='delivery', y='runs' )
    plt.subplot(1,2,2)
    plt.histogram(inning_2, x='delivery', y='runs')

    #return inning_2[:10]
#print plot_innings_runs_histogram()
plt.show()
