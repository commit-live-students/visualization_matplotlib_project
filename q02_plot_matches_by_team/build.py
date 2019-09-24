import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    gdf_ipl = ipl_df.groupby('batting_team')
    match_by_team = gdf_ipl['match_code'].nunique()
    print match_by_team
    match_by_team.plot(kind='bar')
    plt.show()
