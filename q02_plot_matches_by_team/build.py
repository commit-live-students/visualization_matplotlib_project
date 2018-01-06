import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    #ipl_df['count'] = 1
    #bardt = ipl_df.pivot_table('delivery', aggfunc = np.size, index ='batting_team')
    test = ipl_df.groupby('batting_team').agg({'match_code': 'nunique'})
    plt.title('matches_by_the_team')
    plt.xlabel('batting team')
    plt.ylabel('no of matches')
    bardt.plot(kind = 'bar')
    plt.show()

# Solution
