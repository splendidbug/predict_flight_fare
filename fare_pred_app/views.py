from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
from datetime import timedelta
import sys


def index(request):
    

    return render(request, "fare_pred_app/flight.html")

def ticket(request):

    
    name = request.POST['first_name']
    age = request.POST['age']
    sex = request.POST['sex']
    dep_date = request.POST['dep_date']
    dep_time = request.POST['dep_time']
    source = request.POST['source']
    source1 = source
    arr_date = request.POST['arr_date']
    arr_time = request.POST['arr_time']
    destination = request.POST['des']
    destination1 = destination
    stops = request.POST['stoppage']
    airline = request.POST['airline']
    
   
    loaded_rf = joblib.load("random_forest1.joblib")
    all_cols = ['Date',	'Dep_Time',	'Arrival_Time',	'Total_Stops',	'Month',	'Airline_Air Asia',	'Airline_Air India',	'Airline_GoAir',	'Airline_IndiGo',	'Airline_Jet Airways',	'Airline_Multiple carriers',	'Airline_SpiceJet',	'Airline_Vistara',	'Destination_Banglore',	'Destination_Cochin',	'Destination_Delhi',	'Destination_Hyderabad',	'Destination_Kolkata',	'Destination_New Delhi',	'Source_Banglore',	'Source_Chennai',	'Source_Delhi',	'Source_Kolkata',	'Source_Mumbai']
    df_pred = pd.DataFrame(columns=all_cols)
    df_pred.loc[0]=0
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



    
   
    content = {'name':name, 'age': age, 'sex':sex, 'dep_date': dep_date, 'dep_time': dep_time, 'arr_date':arr_date, 'arr_time': arr_time, 'source': source1, 'destination': destination1, 'stoppage': stops, 'airline': airline, 'fare':out}
    return render(request, "fare_pred_app/ticket.html", content)