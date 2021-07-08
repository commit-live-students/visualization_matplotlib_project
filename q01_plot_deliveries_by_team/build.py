import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    team_deliveries=ipl_df[['batting_team','delivery']]
    ipl_bat_group=pd.groupby(team_deliveries,by='batting_team')
   # print(team_deliveries)
   # print(ipl_bat_group.count().head())  
    ipl_bat_group.plot(kind='bar')
    plt.show()
