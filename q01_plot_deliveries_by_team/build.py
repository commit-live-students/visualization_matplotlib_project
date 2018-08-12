import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
df=ipl_df[['team1','delivery']].groupby('team1').count().plot.bar()
plt.show()
