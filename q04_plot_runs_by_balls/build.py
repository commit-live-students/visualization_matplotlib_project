import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)
ipl_df['balls']=1
def plot_runs_by_balls():
	data1=ipl_df.groupby('batsman').agg({'balls':'sum','runs':'sum'})
	plt.scatter(data1['balls'],data1['runs'])
	plt.show()
