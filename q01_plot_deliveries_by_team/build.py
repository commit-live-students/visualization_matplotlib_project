import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
path = "data/ipl_dataset.csv"

path1 = "data/ipl_dataset.csv"

path2 = "data/weather_2012.csv"

def read_csv_data_to_df(path):
    return pd.read_csv(path)
