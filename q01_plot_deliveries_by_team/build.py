import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

# Solution
def plot_deliveries_by_team():

    df = ipl_df.loc[:,['batting_team','delivery']]
    df['count'] = 1

    pdf = df.pivot_table('count',aggfunc = np.size,index = 'batting_team')
    deliv_by_team = pdf.plot(kind = 'bar')
    deliv_by_team.xlabel('batting_team')
    deliv_by_team.ylabel('deliveries')
    #return deliv_by_team
    plt.show()




#print plot_deliveries_by_team()
