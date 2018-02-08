import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    no_of_matches_played= ipl_df.pivot_table('match_code', aggfunc='nunique',index='batting_team')
    no_of_matches_played.plot(kind ='bar')
    plt.show()
