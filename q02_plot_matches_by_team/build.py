import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    uni_df = ipl_df.groupby('batting_team').nunique()
    plt.bar(np.arange(len(uni_df.index)), uni_df['match_code'])
    plt.xticks(np.arange(len(uni_df.index)), uni_df.index, rotation = 45)
    plt.show()
