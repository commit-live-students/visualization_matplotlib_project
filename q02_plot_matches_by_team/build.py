import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    a = ipl_df[['batting_team','match_code']]
    b = a.groupby(by='batting_team').nunique()
    b.plot(kind = 'bar')
    plt.show()


# Solution
