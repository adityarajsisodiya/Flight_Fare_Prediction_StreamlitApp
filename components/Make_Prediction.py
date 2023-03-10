#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def predict(model,input_data):
    data=prepare_data(input_data)
    predicted_result=model.predict(data)
    return int(predicted_result[0])
    
def prepare_data(input_data):
    airline=dict({"IndiGo":1,
                  "Air India":2,
                  "Jet Airways":3,
                  "SpiceJet":4,
                  "Multiple carriers":5,
                  "GoAir":6,
                  "Vistara":7,
                  "Air Asia":8})
    source=dict({"Banglore":1,
                 "Kolkata":2,
                 "Delhi":3,
                 "Chennai":4,
                 "Mumbai":5})
    destination=dict({"New Delhi":1,
                      "Banglore":2,
                      "Cochin":3,
                      "Kolkata":4,
                      "Delhi":5,
                      "Hyderabad":6})
    stopage=dict({"non-stop":0,
                   "1 stop":1,
                   "2 stops":2,
                   "3 stops":3,
                   "4 stops":4})
    import numpy as np
    import pandas as pd
    import time
    current_time=time.ctime().split()[3]
    row_data=list((int(airline.get(input_data[0])),
                   int(source.get(input_data[1])),
                   int(destination.get(input_data[2])),
                   int(stopage.get(input_data[3])),
                   int(pd.to_datetime(input_data[4]).day),
                   int(pd.to_datetime(input_data[4]).month),
                   int(current_time.split(":")[0]),
                   int(current_time.split(":")[1])))
    data=np.array(row_data,ndmin=2)
    return data

