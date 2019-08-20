import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_innings_runs_histogram():
    plt.close('all') # restting the canvas
    plot_data = ipl_df[['batting_team','inning','runs']].groupby(['batting_team','inning']).agg({np.sum})
    plot1 = plot_data.query('inning == 1')
    plot2 = plot_data.query('inning == 2')
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
    plot1.plot(kind='hist', ax=ax1)
    plot2.plot(kind='hist', ax=ax2)
    f.autofmt_xdate() # To rotate x axis labels
    #plt.show()
    return None
