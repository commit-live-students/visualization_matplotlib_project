from matplotlib import pyplot as plt
import pandas as pd

def plot_deliveries_by_team():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    runs=ipl_data.groupby(['match_code','batsman'])['runs'].sum().to_frame()
    balls=ipl_data.groupby(['match_code','batsman'])['delivery'].count().to_frame()
    ans=pd.merge(balls,runs, left_index=True,right_index=True)
    plt.scatter(ans['delivery'],ans['runs'])
    plt.show()
    return 

plot_deliveries_by_team()


