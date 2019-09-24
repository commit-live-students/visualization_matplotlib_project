import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_deliveries_by_team():
    x = ipl_df.groupby(['batting_team'])['delivery'].count()
    x = pd.DataFrame(x)
    x.plot(kind='bar')
    plt.xlabel('Batting Team')
    plt.ylabel('Deliveries')
    plt.title('Deliveried by Team')
    plt.show()
