from matplotlib import pyplot as plt
import pandas as pd

def plot_innings_runs_histogram():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    inning1=ipl_data[ipl_data['inning']==1]
    inning2=ipl_data[ipl_data['inning']==2]
    hist1=inning1.groupby(['match_code'])['runs'].sum()
    hist2=inning2.groupby(['match_code'])['runs'].sum()
    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2)
    ax1.hist(hist1)
    ax2.hist(hist2)
    plt.show()
    return


