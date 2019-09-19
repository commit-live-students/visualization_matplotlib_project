import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    ns = ipl_df.groupby(by='batting_team').nunique()
    ns['match_code'].plot(kind = 'bar')
    plt.show()
