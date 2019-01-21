# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


ipl_df.columns
# Solution
def plot_deliveries_by_team():
    delivery_count = ipl_df.groupby(['batting_team'])['delivery'].agg('count')
    plt.bar(ipl_df['batting_team'].value_counts(), delivery_count,align='center', alpha=0.5)
#ipl_df['runs'].groupby('match_code').agg('count')
#ipl_df.groupby(['batting_team','delivery'].count()
plot_deliveries_by_team()
#ipl_df.batting_team.unique != 'Mumbai Indians'
#ipl_df['batting_team'].nunique
#ipl_df.groupby(['batting_team'])['delivery'].agg('count')

ipl_df['batting_team'].value_counts()

