# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
df = ipl_df.groupby('batting_team').nunique()
plt.bar(df.index, df['match_code'])
plt.title('Total number of matches played by each team')
plt.xlabel('Batting Teams')
plt.ylabel('Matches Count')
plt.xticks(rotation = 90)
plt.show()


