import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    code_team = ipl_df[['match_code' , 'batting_team']]

    group_code_team = code_team.groupby(['batting_team','match_code'])
    unique_team = group_code_team['batting_team'].unique()
    count = unique_team.value_counts().sort_index()

    count.plot(kind = 'bar',title='matches by team' ,  )
    plt.show()

plot_matches_by_team()

# Solution
