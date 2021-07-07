# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    y = ipl_df.groupby(['batting_team'])['match_code'].nunique()
    x= np.arange(len(y.index))

    plt.bar(x,y)
    plt.xticks(x,y.index,rotation = 90)
    plt.xlabel('Teams')
    plt.ylabel('No. of matches played')
    plt.title('No. of matches played by each team')
    plt.show()
    
plot_matches_by_team()



