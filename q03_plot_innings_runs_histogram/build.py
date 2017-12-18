import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
def plot_innings_runs_histogram():
	data1=ipl_df.pivot_table('runs',aggfunc=sum,index=['match_code'],columns='inning')
	plt.hist(data1)
	plt.show()
