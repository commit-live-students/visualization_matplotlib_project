# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_deliveries_by_team():
    x = ipl_df['batting_team'].value_counts().index
    y = ipl_df['batting_team'].value_counts().values
    plt.bar(x,y)
    plt.xticks(rotation = '90')
    plt.show()
    
plot_deliveries_by_team()



# #ipl_df.columns
# x = ipl_df['batting_team'].unique()
# y = ipl_df['delivery'].count()
# plt.bar(x,y)
plt.show()



# #ipl_df.columns
# x = ipl_df['batting_team'].unique()
# y = ipl_df['delivery'].count()
# plt.bar(x,y)
plt.show()

# #ipl_df.columns
# x = ipl_df['batting_team'].unique()
# y = ipl_df['delivery'].count()
plt.bar(x,y)
plt.show()



print('e')
# %load q01_plot_deliveries_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


x = ipl_df['batting_team'].value_counts().index
y = ipl_df['batting_team'].value_counts().values
plt.bar(x,y)
plt.xticks(rotation = '90')
plt.show()
plt.xticks()




