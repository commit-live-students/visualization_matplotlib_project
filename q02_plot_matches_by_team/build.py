import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    action_count=ipl_df.pivot_table('match_code',aggfunc='nunique',index='batting_team')
    action_count.plot(kind='bar')
    plt.show()
