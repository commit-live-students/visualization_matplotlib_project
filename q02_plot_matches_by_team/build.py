from matplotlib import pyplot as plt
import pandas as pd

def plot_deliveries_by_team():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    match_counts=ipl_data.groupby(['batting_team'])['match_code'].nunique()
    x_series=match_counts.index.values
    y_series=match_counts.values
    plt.bar(x_series,y_series)
    plt.show()
    return
   
plot_deliveries_by_team()

