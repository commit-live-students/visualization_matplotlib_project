import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    df=ipl_df[['match_code','batting_team']]
    #new_df=df.pivot_table('match_code',index='batting_team',aggfunc='nunique')
    new_df = df.groupby('batting_team').nunique()
    new_df['match_code'].plot(kind='bar')
    plt.show()
