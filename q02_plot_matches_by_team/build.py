import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_matches_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    matches = ipl_df.groupby('batting_team')['match_code'].nunique()
    matches.plot('bar')
    plt.show()



# Solution
