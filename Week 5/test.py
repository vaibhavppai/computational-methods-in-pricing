import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import matplotlib.ticker

# %matplotlib inline

#Linear Regression
from sklearn import linear_model

#used for 3D plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#igore warning
import warnings
warnings.filterwarnings("ignore")

from gradient import *
from objFunc1 import *

df = pd.read_csv('swapLiborData.csv')

# convert number to datatime format
for i in range(df.shape[0]):
    df.loc[i, 'Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.loc[i, 'Date'], 'D')

df.head(5)