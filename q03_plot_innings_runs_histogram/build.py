import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    # Creating a desired data into dataframe
    df00 = pd.pivot_table(ipl_df,values='runs', index=['batting_team'],columns='inning',aggfunc=np.sum)

    # Creating plot
    # The reason for creating a bar plot as opposed to histogram is that the question required us to assess
    # the score of each team; which generates very few data instances (<30); and it's easy to eyeball over the bar charts
    plt.figure()
    plt.subplot(2,1,1)
    df00[1].plot(kind='bar')
    plt.show()
    plt.subplot(2,1,2)
    df00[2].plot(kind='bar')
    plt.show()
    return None
