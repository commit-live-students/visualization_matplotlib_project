import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    b1 = ipl_df.groupby('batting_team').count()
    plt.bar( range(0, len(b1.index)) , b1['delivery'] )
    plt.xticks(range(0, len(b1.index)), b1.index, rotation=90)
    plt.show()

plot_deliveries_by_team()
