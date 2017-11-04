import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    new_df = ipl_df.groupby(['match_code','batting_team'],as_index=False).count()[['batting_team','delivery']]
    new_df.groupby('batting_team',as_index=False).sum()
    delivery_df.plot(kind='bar')
    plt.show()
