import re
import numpy as np
import pandas as pd

DATA_IN_PATH = "data/data_out.csv"


COL_VALUES = ["x", "y", "z","xg","yg","zg"] #input file needs to always have obj as last column
N_CLASSES = 5 #note that objects must be numbered from 0 to N_CLASSES
ROWS = 80 #how many lines per image snapshot
COLS = len(COL_VALUES)

print "loading ", DATA_IN_PATH
data=pd.read_csv(DATA_IN_PATH, names = COL_VALUES + ["obj"])
print "random portions of the data set:"
print data.loc[7000000:7000010,COL_VALUES + ["obj"]]
print data.loc[1000:1010,COL_VALUES + ["obj"]]
print data.loc[50000:50010,COL_VALUES + ["obj"]]

print data.describe()