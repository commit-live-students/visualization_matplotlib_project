# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    new_data =  ipl_df.groupby('batting_team').agg({'match_code':'nunique'})    
    x= new_data.index
    y=new_data['match_code']
    plt.figure(figsize=(15,25))
    plt.title('IPL Team Matches')
    plt.xlabel('Teams')
    plt.ylabel('Matches played')
    plt.xticks( rotation=45)
    plt.bar(x,y)

