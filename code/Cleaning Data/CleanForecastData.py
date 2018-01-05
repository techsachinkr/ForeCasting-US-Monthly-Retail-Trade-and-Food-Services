"""
@author: SACHIN
"""
import pandas as pd
from pandas import Series
import matplotlib.pylab as plt
import numpy as npy
import os
current_file = os.path.abspath(os.path.dirname('__file__'))
datavalues = pd.read_csv('../../data/datavalues.csv')
datatypes = pd.read_csv('../../data/datatypes.csv')
dateparse = lambda dates: pd.datetime.strptime(dates, '%b-%y')
timeperiods = pd.read_csv('../../data/timeperiods.csv',parse_dates=['per_name'],date_parser=dateparse)
categories = pd.read_csv('../../data/categories.csv')


datavalues = pd.merge(left = datavalues,right = timeperiods,how = 'left',on=['per_idx'])

#Monthly Sales


monthlysalesData= pd.DataFrame(datavalues.loc[datavalues['dt_idx'] == 1])

monthlysalesData=monthlysalesData.drop('per_idx',axis=1)
monthlysalesData=monthlysalesData.drop('cat_idx',axis=1)

monthlysalesData=monthlysalesData.loc[monthlysalesData['is_adj'] == 0]

monthlysalesData=monthlysalesData.drop('dt_idx',axis=1)

monthlysalesData=monthlysalesData.drop('et_idx',axis=1)
monthlysalesData=monthlysalesData.drop('is_adj',axis=1)

missingSalesVal=monthlysalesData.loc[monthlysalesData['val'] == '(S)']
monthlysalesData=monthlysalesData.loc[monthlysalesData['val'] != '(S)']
monthlysalesData['val']=monthlysalesData['val'].astype(float)
monthlysalesData=monthlysalesData.groupby(monthlysalesData.per_name).sum()