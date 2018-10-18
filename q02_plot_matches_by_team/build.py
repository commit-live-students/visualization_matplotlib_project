import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    count_matches = ipl_df.groupby(['batting_team']).agg('nunique')['match_code']
    count_matches.plot(kind = 'bar')
    plt.show();
    
plot_matches_by_team()




