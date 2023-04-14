# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:16:32 2023

@author: ANTRIKSH
"""

import streamlit as st
import streamlit_analytics



with streamlit_analytics.track():

    Container = st.container()
    Name = st.text_input(label="What is your name")
    click = st.button(label="Save the name",key="Name")
    if len(Name) > 2 and click:
        Container.subheader(Name+" is a student of the great Antriksh")
        
    streamlit_analytics.start_tracking()    

streamlit_analytics.track(save_to_json="file.json")