#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os
from components.Make_Prediction import predict


# In[ ]:

path=os.path.abspath("flight_model.pkl")
file=open(path,"rb")
model=pickle.load(file)


# In[ ]:


airline_list=list(("IndiGo","Air India","Jet Airways","SpiceJet","Multiple carriers","GoAir","Vistara","Air Asia"))
source_list=list(("Banglore","Kolkata","Delhi","Chennai","Mumbai"))
destination_list=list(("New Delhi","Banglore","Cochin","Kolkata","Delhi","Hyderabad"))
stopage_list=list(("non-stop","1 stop","2 stops","3 stops","4 stops"))


# In[ ]:


st.title("Flight Fare Prediction App")
st.header("Search Flight")
with st.form(key="form1",clear_on_submit=True):
    col1,col2=st.columns(2)
    with col1:
        travel_date=st.date_input(label="Travel Date")
    with col2:
        return_date=st.date_input(label="Return Date (optional)")
    col1,col2=st.columns(2)
    with col1:
        source=st.selectbox('Source City', source_list)
    with col2:
        destination=st.selectbox('Destination City', destination_list)
    col1,col2=st.columns(2)
    with col1:
        num_of_stop=st.selectbox('Stopage', stopage_list)
    with col2:
        airline=st.selectbox('Which Airline you want to Travel', airline_list)
    button=st.form_submit_button("Predict Price")
    if(button):
        input_data=list((airline,source,destination,num_of_stop,travel_date,return_date))
        result=predict(model,input_data)
        st.success(result)

