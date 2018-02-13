import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():

    a = ipl_df.pivot_table('runs',aggfunc = np.sum,index = 'match_code',columns = 'inning')
    a.plot(kind='hist')
    plt.show()




#print plot_innings_runs_histogram()
