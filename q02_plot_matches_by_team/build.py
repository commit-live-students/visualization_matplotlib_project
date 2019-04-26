import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    d2 = ipl_df.groupby('batting_team')['match_code'].agg('nunique')
    plt.bar( range(0, len(d2.index)) , d2.values )
    plt.xticks(range(0, len(d2.index)), d2.index, rotation=90)
    plt.show()

plot_matches_by_team()
