import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    ipl_df1 = ipl_df.groupby('team1').match_code.nunique()
    ipl_df1.plot(kind='bar')
    plt.show()
    return
# Solution
