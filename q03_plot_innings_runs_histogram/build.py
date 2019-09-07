import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    df = ipl_df.groupby(['match_code','inning'])['total'].sum()
    df1 = pd.DataFrame(df)
    df1.reset_index(inplace=True)
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.hist(df1[df1['inning']==1]['total'])
    ax2.hist(df1[df1['inning']==2]['total'])
    plt.show()
