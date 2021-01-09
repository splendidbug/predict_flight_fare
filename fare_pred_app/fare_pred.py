# -*- coding: utf-8 -*-
"""fare_pred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OfcIJuP2W1x6bcVu1Dqm7D5m0w5xCTsl
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
from datetime import timedelta
import sys

loaded_rf = joblib.load("random_forest1.joblib")

all_cols = ['Date',	'Dep_Time',	'Arrival_Time',	'Total_Stops',	'Month',	'Airline_Air Asia',	'Airline_Air India',	'Airline_GoAir',	'Airline_IndiGo',	'Airline_Jet Airways',	'Airline_Multiple carriers',	'Airline_SpiceJet',	'Airline_Vistara',	'Destination_Banglore',	'Destination_Cochin',	'Destination_Delhi',	'Destination_Hyderabad',	'Destination_Kolkata',	'Destination_New Delhi',	'Source_Banglore',	'Source_Chennai',	'Source_Delhi',	'Source_Kolkata',	'Source_Mumbai']

df_pred = pd.DataFrame(columns=all_cols)
df_pred.loc[0]=0



dep_date = sys.argv[1]
dep_time = sys.argv[2]
#arr_date = '23/05/21'
arr_time = sys.argv[3]
source = sys.argv[4]
destination = sys.argv[5]
stops = sys.argv[6]
airline = sys.argv[7]

day = int(dep_date.split('/')[0])
month = int(dep_date.split('/')[1])
dep_h = int(dep_time.split(':')[0])
dep_m = int(dep_time.split(':')[1])
arr_h = int(arr_time.split(':')[0])
arr_m = int(arr_time.split(':')[1])

delta = timedelta(hours=int(dep_time.split(':')[0]), minutes=int(dep_time.split(':')[1]))
Dep_Time = delta.total_seconds()/60

delta = timedelta(hours=int(arr_time.split(':')[0]), minutes=int(arr_time.split(':')[1]))
Arrival_Time = delta.total_seconds()/60


airline = 'Airline_' + airline
destination = 'Destination_' + destination
source = 'Source_' + source

df_pred['Total_Stops'] = stops
df_pred['Date'] = day
df_pred['Month'] = month
df_pred['Dep_Time'] = Dep_Time
df_pred['Arrival_Time'] = Arrival_Time

lst = [airline, destination, source]
df_pred[lst]=1

df_pred

y_pred = loaded_rf.predict(df_pred)
out=y_pred[0]
print(out)
