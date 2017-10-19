import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    team_delivery_counts = ipl_df.groupby(by='batting_team').count()
    row_count = team_delivery_counts.shape[0]
    x_series = np.arange(0, row_count, 1)
    plt.figure(figsize=(20,5))
    plt.bar(x_series, team_delivery_counts.delivery)
    plt.xlabel('Batting Team')
    plt.ylabel('# of Deliveries')
    plt.title('Deliveries by Team Plot')
    plt.xticks(x_series, team_delivery_counts.index, rotation=45)
    plt.show()
