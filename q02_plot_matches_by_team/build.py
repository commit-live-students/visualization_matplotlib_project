#%load q02_plot_matches_by_team/build.py

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

ifl_df=pd.read_csv('./data/ipl_dataset.csv')

def plot_matches_by_team():
    gr=ifl_df.groupby('batting_team')['match_code'].nunique()
    gr.plot(kind='bar',title=' total number of matches played by each team')

    plt.xlabel('batsman')
    plt.ylabel('matches played')

    plt.show()
    
plot_matches_by_team()
    
    


