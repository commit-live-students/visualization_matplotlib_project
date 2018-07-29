# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#Function Create
def plot_runs_by_balls():
    ''' Analyze correlation betweem balls and runs made by a batsman'''
    
    #Subset dataframe for one batsman
    ipl_df2 = ipl_df[ipl_df['batsman'] == 'ST Jayasuriya']

    #extrating runa and balls from above series by groupby
    yruns = ipl_df2[['match_code','runs']].groupby(['match_code']).sum()['runs']
    xball = ipl_df2[['match_code','delivery']].groupby(['match_code']).count()['delivery']

    #plotting the charts
    plt.scatter(xball , yruns)
    plt.xlabel('No of balls')
    plt.ylabel('No of runs')
    plt.show()

#Function call
plot_runs_by_balls()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#Function Create
def plot_runs_by_balls():
    ''' Analyze correlation betweem balls and runs made by a batsman'''
    
    #Subset dataframe for one batsman
    ipl_df2 = ipl_df[ipl_df['batsman'] == 'ST Jayasuriya']

    #extrating runa and balls from above series by groupby
    yruns = ipl_df2[['match_code','runs']].groupby(['match_code']).sum()['runs']
    xball = ipl_df2[['match_code','delivery']].groupby(['match_code']).count()['delivery']

    #plotting the charts
    plt.scatter(xball , yruns)
    plt.xlabel('No of balls')
    plt.ylabel('No of runs')
    plt.show()

#Function call
plot_runs_by_balls()
help(pd.groupby)


