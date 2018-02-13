import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():

    a = ipl_df.pivot_table('runs',aggfunc = np.sum,index = 'match_code',columns = 'inning')
    a.plot(kind='hist')
    plt.show()



'''def plot_innings_runs_histogram():
    df1 = ipl_df.loc[:,['match_code','inning','runs']]
    df2 = pd.pivot_table(data=df1.loc[:,['match_code', 'runs']], index='match_code', columns=df1.loc[:,'inning'], aggfunc='count')
    #df2.plot(kind='hist')
    #plt.show()
    return df2[:5]'''

#print plot_innings_runs_histogram()
