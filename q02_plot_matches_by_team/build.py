# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('./data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    data = ipl_df[['match_code','batting_team']]
    grp = data.groupby(data['batting_team'])
    newgrp = data.groupby('batting_team')['match_code'].nunique()
    x_label = range(1,14)
    plt.bar(x_label,newgrp)
    plt.xticks(x_label, newgrp.index, rotation=90)
    plt.show()
    return
