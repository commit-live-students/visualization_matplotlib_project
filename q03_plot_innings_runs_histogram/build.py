# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def get_data():
    first_inning = ipl_df[ipl_df['inning'] == 1]
    second_inning = ipl_df[ipl_df['inning'] == 2]
    
    fi_df = pd.DataFrame(
        first_inning.groupby(['match_code']).sum()['runs'])

    se_df = pd.DataFrame(
        second_inning.groupby('match_code').sum()['runs'])
    
    return fi_df, se_df
    
def plot_innings_runs_histogram():
    f,s = get_data()
#     print(f,s)
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.hist(f, bins=12)
    ax1.set_title('First Inning Runs')
    plt.xticks(rotation=90)
    ax2.hist(s, bins=12)
    ax2.set_title('Second Inning Runs')
    plt.xticks(rotation=90)
    plt.show()

# get_data()[0]
plot_innings_runs_histogram()





