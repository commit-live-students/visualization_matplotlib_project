# %load q03_plot_innings_runs_histogram/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_innings_runs_histogram():
    for i in range(1,3,1):
        plt.subplot(1,2,i)
        ipl_df.groupby(['match_code','inning']).runs.agg('sum')[i::2].plot(kind='hist')
        plt.xlabel('Runs in innings -'+str(i))
    plt.show()
        
plot_innings_runs_histogram()




#Alternate simple to understand solution -

#Standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading the csv file into dataframe
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

#Reserving space for each histogram in canvas by using subplot function.
plt.subplot(1,2,1)

#To check the dataframe output for first innings
#ipl_df.groupby(['match_code','inning']).runs.agg('sum')[0::2] 

#histogram for 1st innings
ipl_df.groupby(['match_code','inning']).runs.agg('sum')[0::2].plot(kind='hist')
plt.xlabel('Runs in innings - 1')

#Logic same as above
plt.subplot(1,2,2)
ipl_df.groupby(['match_code','inning']).runs.agg('sum')[1::2].plot(kind='hist')
plt.xlabel('Runs in innings - 2')

plt.show()


