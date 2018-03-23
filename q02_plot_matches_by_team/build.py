import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
    ipl_match_count = ipl_df.groupby(['batting_team']).agg('nunique')
    plt.bar(ipl_match_count.index,ipl_match_count.match_code)
    plt.title('Count of match played by each team, IPL')
    plt.xlabel('Team')
    plt.ylabel('Match frequency')
    plt.xticks(ipl_match_count.index,rotation=90)
    plt.show()
