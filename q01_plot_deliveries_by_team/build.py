import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_deliveries_by_team():
    team_names = ipl_df.loc[]
    x_axis =
    y_axix =
    plt.plot(x_series, y_series)
    plt.title('Total Number Of Deliveries')
    plt.xlabel('Batting Team')
    plt.ylabel('Count Of Deliveries')
    plt.xticks(x_series, calendar_months, rotation=45)
    plt.show()

# Solution
