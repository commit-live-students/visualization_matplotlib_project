import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_runs_by_balls():
    plot_data = ipl_df[['batsman', 'delivery', 'runs']].groupby(['batsman']).agg(
        {'delivery':np.count_nonzero, 'runs':np.sum})
    plt.close('all')
    f,ax = plt.subplots()
    plot_data.plot(kind='scatter', x='delivery', y='runs', ax=ax)
    f.suptitle('Balls vs Runs')
    plt.xlabel = 'Balls played' # Not showing up
    plt.ylabel = 'Runs Scored' # Not showing up
    #plt.show()
    return None
