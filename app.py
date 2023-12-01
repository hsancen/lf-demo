# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:12:46 2023

@author: hugos

Below is how to run streamlit app from spyder using IPython Console
import os
os.system("streamlit run app.py")

https://docs.streamlit.io/library/api-reference
https://github.com/PablocFonseca/streamlit-aggrid
https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/
"""

import streamlit as st
import pandas as pd

ratings_df = pd.read_csv('ratings.csv')
pricing_df = pd.read_csv('pricing.csv')


rating_actions = st.sidebar.multiselect(
    'Apply filters:',
    ratings_df.rating_action.unique())

table_data = ratings_df[ratings_df.rating_action.isin(rating_actions)]

st.dataframe(table_data, hide_index = True, use_container_width=True)

table_data_isins = table_data['isin'].to_list()
chart_data = pricing_df[pricing_df['isin'].isin(table_data_isins)]

st.line_chart(
   chart_data, x="price_date", y=["bid"]
)