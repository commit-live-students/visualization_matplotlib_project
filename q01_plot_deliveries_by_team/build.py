# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    
    
    
    plt.bar(ipl_df['batting_team'].unique(), ipl_df['batting_team'].value_counts())
    

    plt.title('Number of Deliveries of each team')
    plt.xlabel('Batting Team')
    plt.ylabel('Counts of Deliveries')

    plt.xticks(ipl_df['batting_team'].unique(), rotation=90)
    
    plt.yticks(ipl_df['batting_team'].value_counts())
    
    

    plt.show()
    
   
    
    
plot_deliveries_by_team()
    



