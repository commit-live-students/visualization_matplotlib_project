import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution

def plot_deliveries_by_team():
    ipl_dict = {}
    for i in (ipl_df['batting_team'].value_counts()).index:
        freq =  ((ipl_df['batting_team']==i).value_counts())
        actual_delivery = freq.get(True)
        ipl_dict[i]=actual_delivery
    teams = list(ipl_dict.keys())
    deliveries = list(ipl_dict.values())
    plt.bar(range(len(ipl_dict)),deliveries,tick_label=teams)
    plt.show()
