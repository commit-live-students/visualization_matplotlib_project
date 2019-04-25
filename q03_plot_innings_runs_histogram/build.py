import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():


        inning_runs = ipl_df.groupby(['match_code','inning'])['runs'].sum()



        plt.subplot(121)
        plt.hist( inning_runs[:,1] , bins=10 , )
        plt.title('1st innings')
        plt.xlabel('runs')

        plt.subplot(122)
        plt.hist(inning_runs[:,2] , bins = 10)
        plt.title('2nd innings')
        plt.xlabel('runs')


        plt.show()

plot_innings_runs_histogram()
