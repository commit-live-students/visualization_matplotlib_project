import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():

    s = DataFrame(ipl_df['total'].groupby([ipl_df['match_code'], ipl_df['batsman']]).sum())
    s1 = DataFrame(ipl_df['delivery'].groupby([ipl_df['match_code'], ipl_df['batsman']]).count())
    #s3 = pd.DataFrame( np.hstack((s1.values, s2.values))
    #plt.hist(s)
    #plt.show()

    runs_scored = pd.pivot_table(ipl_df, values='total', index=['match_code', 'batsman','inning'], \
                      aggfunc=np.sum)
    balls_played = pd.pivot_table(ipl_df, values='delivery', index=['match_code', 'batsman','inning'], \
                      aggfunc= len)
    data = pd.concat(runs_scored, balls_played)
    print data
    #plt.hist(data['delivery'])
    #plt.hist()

plot_innings_runs_histogram()
