# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_deliveries_by_team():
    df=ipl_df[['batting_team','delivery']].groupby('batting_team').count().reset_index()
    
    x=df['batting_team']
    y=df['delivery']
    
    plt.bar(x,y)
    plt.title('Deliveries By Team')
    plt.xlabel('Team Names')
    plt.ylabel('Deliveries Count')
    plt.show()
   
plot_deliveries_by_team()



