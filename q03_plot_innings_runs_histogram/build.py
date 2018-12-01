import numpy as np
import pandas as  pd
from matplotlib import pyplot as plt

ifl_df=pd.read_csv('./data/ipl_dataset.csv')

def plot_innings_runs_histogram():
    
    gr=ifl_df.groupby(['match_code','inning'])['runs'].sum()
#gr[1::2]

    fig = plt.figure()
    ax = fig.add_subplot(121)
    gr[1::2].plot(kind='hist',title=' total number of runs inning 1')
    ax = fig.add_subplot(122)
    gr[2::2].plot(kind='hist',title=' total number of runs inning 2')

    plt.show()
    
plot_innings_runs_histogram()


