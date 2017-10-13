import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def plot_runs_by_balls() :
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    plt.scatter((ipl_df.delivery.apply(np.int64))*10, (ipl_df.total.apply(np.int64))*10)
    #plt.title('NYC House pricing')
    plt.xlabel('Count of Balls Played')
    plt.ylabel('Total Runs Scored')
    plt.show()

# Solution
