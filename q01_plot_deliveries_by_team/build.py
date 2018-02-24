import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    #pd.pivot_table(data=ipl_df.loc[:,['match_code', 'runs']], index='match_code', columns=ipl_df.loc[:,'runs'], aggfunc='count')
    #each match--> each team--> total deliveries
    df = ipl_df.groupby('batting_team')
    team_total_delivery = df['delivery'].sum()
    #print team_total_delivery
    team_total_delivery.plot( kind='bar')
    plt.show()

plot_deliveries_by_team()
