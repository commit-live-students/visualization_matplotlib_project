import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_matches_by_team():
	data1=ipl_df.groupby('batting_team').agg({'match_code': 'nunique'})
	data1.plot(kind='bar')
	plt.show()
