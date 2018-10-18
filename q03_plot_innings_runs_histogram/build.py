import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_innings_runs_histogram():
    f1_match = ipl_df.groupby(['match_code','inning']).agg('sum')['total']
    f1_match.plot(kind= 'hist', subplots= True)
    plt.show();

plot_innings_runs_histogram()


