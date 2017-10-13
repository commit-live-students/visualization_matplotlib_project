import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def plot_innings_runs_histogram() :
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    #ipl_df[['batting_team']].plot.bar()
    data = ipl_df.groupby('batting_team').date.agg(['nunique'])
    #print data
    data.plot.bar(legend=False)
    plt.show()


# Solution
