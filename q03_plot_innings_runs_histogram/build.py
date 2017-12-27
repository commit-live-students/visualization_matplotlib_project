import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    tablea=ipl_df.pivot_table(values='runs',aggfunc='sum',index=['batsman'] ,columns='match_code' )
    tableb=ipl_df.pivot_table(values='delivery',aggfunc='count',index=['batsman'] , columns='match_code')
    tablec=pd.merge(tablea,tableb)
    tablec.plot(kind='hist')
    plt.show()
