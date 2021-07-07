# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    df=ipl_df.groupby(['batting_team','match_code'], as_index=False)['team1'].count()
    k=pd.DataFrame(df['batting_team'].value_counts()).reset_index()
    k.rename(columns={'index': 'TEAM', 'batting_team': 'Count'}, inplace=True)
    plt.bar(k['TEAM'],k['Count'])
    plt.show()
    



