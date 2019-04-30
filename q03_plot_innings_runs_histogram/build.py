import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    data=ipl_df.groupby(['match_code','inning'])['runs'].agg('sum')

    inning1=data[:,1]
    inning2=data[:,2]
    
    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    fig.tight_layout()
    axes[0].hist(inning1)
    axes[0].set_title('Distribution of runs in 1st innings')
    axes[0].set_xlabel('Runs')
    axes[0].set_ylabel('No. of matches')

    axes[1].hist(inning2)
    axes[1].set_title('Distribution of runs in 2nd innings')
    axes[1].set_xlabel('Runs')
    axes[1].set_ylabel('No. of matches')

    plt.show()
