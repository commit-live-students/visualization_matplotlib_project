from matplotlib import pyplot as plt
import pandas as pd

def plot_deliveries_by_team():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    delivery_counts=ipl_data['batting_team'].value_counts()
    x_series=delivery_counts.index.values
    y_series=delivery_counts.values
    plt.bar(x_series,y_series)
    plt.show()
    return 
   
plot_deliveries_by_team()




