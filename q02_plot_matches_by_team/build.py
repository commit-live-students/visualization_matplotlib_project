# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    
    
    unique_matches = ipl_df.groupby('batting_team').agg('nunique')
    match_count = unique_matches['match_code']
    
    plt.bar(ipl_df['batting_team'].unique(),match_count )
    plt.title('Number of Deliveries of each team')
    plt.xlabel('Batting Team')
    plt.ylabel('Match Count ')
    plt.xticks(ipl_df['batting_team'].unique(), rotation=90)
    
    plt.show()
    
   
    
    
plot_deliveries_by_team()
    


