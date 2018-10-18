import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    count_deliveries = ipl_df.groupby(['batting_team']).agg('count')['delivery']
    count_deliveries.plot(kind = 'bar')
    
    plt.show();
    


plot_deliveries_by_team()



