import streamlit as st
import pandas as pd
import plotly_express as px



st.set_page_config(page_title='Save More',page_icon='💵')



try:
    csvfile = pd.read_csv('save.csv')
except:
    csvfile = pd.DataFrame()






st.title('Save More')



st.sidebar.title('Start Saving')



date = st.sidebar.date_input('Date:')

made = st.sidebar.number_input('Money Made')

spent = st.sidebar.number_input('Money Spent')

if st.sidebar.button('Create/Update'):
    csvfile.loc[0,'Date'] = spent
    csvfile.to_csv('save.csv',index=False)








            




