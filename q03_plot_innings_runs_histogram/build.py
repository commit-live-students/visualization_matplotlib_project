import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    #a = ipl_df.groupby(['match_code', 'inning'])
    #innings_and_runs = a['inning'].sum()
    #print type(innings_and_runs)
    #print innings_and_runs[0]
    #print innings_and_runs

    b = pd.pivot_table(ipl_df, index=['match_code'], values='runs', columns=['inning'], aggfunc=np.sum)
    #print b

    b.plot(kind='hist')
    plt.show()

plot_innings_runs_histogram()
