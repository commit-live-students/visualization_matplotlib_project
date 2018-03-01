import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():

    # Runs scored in first and second innings grouped by match code
    runs_scored = ipl_df.pivot_table('total', aggfunc = np.sum, index=['match_code'], \
                      columns = 'inning').fillna(0)
    #Runs scored in first innings
    runs0 = runs_scored.values[:,0]
    #Runs scored in second innings
    runs1 = runs_scored.values[:,1]

    fig, axs = plt.subplots(1, 2)
    axs[0].hist(runs0)
    axs[1].hist(runs1)
    plt.show()
