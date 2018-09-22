# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    
    y = pd.DataFrame(ipl_df.groupby(by = ['batting_team'])['match_code'].nunique()) 
    plt.bar(y.index,y['match_code'])
    plt.show()

# Solution




