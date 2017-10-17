import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('./data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    inning=ipl_df.groupby('inning').sum()
    print(inning['runs'])
    plt.hist(inning['runs'])
    plt.show()
    return
