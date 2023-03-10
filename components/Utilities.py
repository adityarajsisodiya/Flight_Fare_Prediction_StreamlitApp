#!/usr/bin/env python
# coding: utf-8

# In[1]:


def data_processing(data):
  import pandas as pd
  # Date_of_Journey
  data["Journey_day"]= pd.to_datetime(data.Date_of_Journey, format="%d/%m/%Y").dt.day  
  data["Journey_month"] = pd.to_datetime(data["Date_of_Journey"], format = "%d/%m/%Y").dt.month
  data.drop(["Date_of_Journey"], axis = 1, inplace = True)
    
  # Dep_Time
  data["Dep_hour"] = pd.to_datetime(data["Dep_Time"]).dt.hour
  data["Dep_min"] = pd.to_datetime(data["Dep_Time"]).dt.minute
  data.drop(["Dep_Time"], axis = 1, inplace = True)   
  return data

def data_transformation(data):
    Airline_Mapping=dict({"IndiGo":1,
              "Air India":2,
              "Jet Airways":3,
              "SpiceJet":4,
              "Multiple carriers":5,
              "GoAir":6,
              "Vistara":7,
              "Air Asia":8})
    Source_Mapping=dict({"Banglore":1,
                     "Kolkata":2,
                     "Delhi":3,
                     "Chennai":4,
                     "Mumbai":5})
    Destination_Mapping=dict({"New Delhi":1,
                         "Banglore":2,
                         "Cochin":3,
                         "Kolkata":4,
                         "Delhi":5,
                         "Hyderabad":6})
    stopage_mapping=dict({"non-stop":0,
                     "1 stop":1,
                     "2 stops":2,
                     "3 stops":3,
                     "4 stops":4})
    data["Airline"]=data["Airline"].map(Airline_Mapping)
    data["Source"]=data["Source"].map(Source_Mapping)
    data["Destination"]=data["Destination"].map(Destination_Mapping)
    data["Total_Stops"]=data["Total_Stops"].map(stopage_mapping)
    return data

# In[ ]:




