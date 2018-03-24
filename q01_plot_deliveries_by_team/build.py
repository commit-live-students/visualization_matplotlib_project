import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    ipl_delivery_by_team = ipl_df.groupby(ipl_df.team1).count()
    plt.bar(ipl_delivery_by_team.index,ipl_delivery_by_team.delivery)
    plt.title('Delivery by each team, IPL')
    plt.xlabel('Team')
    plt.ylabel('Delivery')
    plt.xticks(ipl_delivery_by_team.index,rotation=90)
    plt.show()
