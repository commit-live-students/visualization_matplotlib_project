# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

def plot_deliveries_by_team():
    ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
    delv = (ipl_df.groupby(by=('batting_team') )).count()

    delv['delivery'].plot.bar()
    return plt.show()

plot_deliveries_by_team()
# Solution

import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

#ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
#delv = (ipl_df.groupby(by=('match_code') )).count()
#print delv.iloc[:,[0,1,2]]
#print len(ipl_df.match_code.unique())
#delv['delivery'].plot.bar()
#plt.show()


