# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_inning_runs_histogram():
    # storing first inning data
    first_inning_data = ipl_df[ipl_df['inning'] == 1]
    
    #storing second inning data
    second_inning_data = ipl_df[ipl_df['inning']==2]
    
    # grouping first inning data by match code and then select 'runs' columns from it 
    first = first_inning_data.groupby('match_code').sum()['runs']
    
    # grouping second inning data by match code and then select 'runs' column from it
    second = second_inning_data.groupby('match_code').sum()['runs']
    
    #creating figure to draw
    fig = plt.figure()
    
    #creatng supplots in figure
    fig, ax = plt.subplots(1,2)
    
    #drawing histogram in first subplot
    ax[0].hist(first)
    
    #drawing histogram in second subplot
    ax[1].hist(second)
    
    plt.show()
    


plot_inning_runs_histogram()


