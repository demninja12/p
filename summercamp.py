import streamlit as st
import pandas as pd


st.set_page_config(page_title='Peggy Camp',page_icon='⛺')

try:
    csvfile = pd.read_csv('Camp.csv')
except:
    csvfile = pd.DataFrame()

st.title('Peggy Camp')

menu = st.sidebar.selectbox('Students',['Enter Weekly Scores'])

if menu == 'Enter Weekly Scores':

    username = st.text_input('Enter Username:',placeholder='Enter Username:',label_visibility='collapsed')


    column1,column2 = st.columns(2)

    with column1:
        pythonscore = st.number_input('Enter Python Score:',0,100,placeholder='Enter Python Score:')
        roboticsscore = st.number_input('Enter Robotics Score:',0,100,placeholder='Enter Robotics Score:')


    with column2:
        developmentscore = st.number_input('Enter Web Development Score:',0,100,placeholder='Enter Web Development Score:')
        javascore = st.number_input('Enter Problem Java Score:',0,100,placeholder='Enter Problem Java Score:')
    

    if st.button('Submit'):
        total = pythonscore + roboticsscore + developmentscore + javascore
        average = total / 4
        campdict = {'Usename':[username],
                    'Python Score':[pythonscore],
                    'Robotics Score':[roboticsscore],
                    'Web Development Score':[developmentscore],
                    'Java Score':[javascore]}
        camptable = pd.DataFrame(campdict)
        tablesjoin = pd.concat([csvfile,camptable],ignore_index=True)
        tablesjoin.to_csv('camp.csv',index=False)
        st.write('Your Total is',total,'and your Average is',average)
        st.table(csvfile)