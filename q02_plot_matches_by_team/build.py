# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    #create empty canvas to draw 
    fig = plt.figure()
    # groupby batting team then count unique and select match_code(as it uniquely identified matched played)
    match_played = ipl_df.groupby('batting_team').nunique()['match_code']
    #plotting bar
    plt.bar(match_played.index, match_played)
    #rotating x ticks by -90 for easy reading team name
    plt.xticks(rotation = -90)
    plt.show()
    
plot_matches_by_team()



