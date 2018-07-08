# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    grouped_values = ipl_df.groupby('batting_team')
    #print(grouped_values['match_code'].agg('nunique'))
    x_values = grouped_values['match_code'].agg('nunique').index
    y_values = grouped_values['match_code'].agg('nunique').values
    #print(x_values,y_values)
    plt.bar(x_values,y_values)
    plt.xticks(rotation=90)
    #plt.show()


