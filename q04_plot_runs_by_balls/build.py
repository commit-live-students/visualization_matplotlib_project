import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():

    a =ipl_df.pivot_table('runs',aggfunc = np.sum,index = 'batsman')

    b =ipl_df.pivot_table('delivery',aggfunc = np.size,index = 'batsman')
    #c = pd.merge(a,b)
    df = pd.concat([a,b],axis=1)

    df.plot(x='delivery',y='runs',kind='scatter')
    plt.show()

#print plot_runs_by_balls()
