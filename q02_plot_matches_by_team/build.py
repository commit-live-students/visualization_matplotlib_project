# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Function Create
def plot_matches_by_team():
    '''Function to plot matches for each team'''
    #dataframe for only teams and matches
    match=ipl_df[['batting_team','match_code']]
    #using unique value function for team and match combination 
    yaxis = match.groupby(['batting_team']).nunique()['match_code']
    #x axis to get indiex which is teams
    xaxis = yaxis.index

    #plot bar chart with labels
    plt.bar(xaxis,yaxis, label = '# Matches')
    plt.xticks(rotation = '90')
    plt.legend()
    plt.show()
    
#Function call 
plot_matches_by_team()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Function Create
def plot_matches_by_team():
    '''Function to plot matches for each team'''
    #dataframe for only teams and matches
    match=ipl_df[['batting_team','match_code']]
    #using unique value function for team and match combination 
    yaxis = match.groupby(['batting_team']).nunique()['match_code']
    #x axis to get indiex which is teams
    xaxis = yaxis.index

    #plot bar chart
    plt.bar(xaxis,yaxis, label = '# Matches')
    plt.xticks(rotation = '90')
    plt.legend()
    plt.show()
    
#Function call 
plot_matches_by_team()


