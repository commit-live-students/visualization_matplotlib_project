# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    new_data = ipl_df.groupby('batting_team').agg({'delivery':'sum'})
    x= new_data.index
    y=new_data['delivery']
    plt.figure(figsize=(15,25))
    plt.title('IPL Team Performance')
    plt.xlabel('Teams')
    plt.ylabel('Deliveries')
    plt.xticks( rotation=45)
    plt.bar(x,y)





