# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)



# Solution
def plot_matches_by_team():
    df = ipl_df[['batting_team', 'match_code']].drop_duplicates()
    df.set_index('match_code', inplace=True)


    df['batting_team'].value_counts().plot(kind='bar')
    
plot_matches_by_team()






