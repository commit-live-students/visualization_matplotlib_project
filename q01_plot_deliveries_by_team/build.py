# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    
    df=ipl_df.groupby('batting_team', as_index=False)['delivery'].count()
    plt.bar(df['batting_team'] ,df['delivery'])
    plt.show()
# Solution




