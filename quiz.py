import streamlit as st
import pandas as pd

st.set_page_config(page_title='Quiz',page_icon='❓')

try:
    quizscore = pd.read_csv('quiz.csv')
except:
    quizscore = pd.DataFrame()




score = 0

username = st.text_input('Enter Username:',placeholder='Enter Username:',label_visibility='collapsed')
if st.checkbox('Start Quiz'):
    if username:
        quizscore.loc[0,'Username'] = username
        quizscore.to_csv('quiz.csv',index=False)



        q1 = if st.sidebar.checkbox('Question 1'):
]



        if st.sidebar.checkbox('Question 2'):
                st.subheader('When was Roblox Created')
                st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                options2 = st.radio('Question 2',['2000','2002','2004','2006'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=2):
                    if options2 == '2006':
                        try:
                            quizscore.loc[0,'Score'] +=5
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =5
                            quizscore.to_csv('quiz.csv',index=False)            
        
        if st.sidebar.checkbox('Question 3'):
            st.subheader('Who was the First Player on Roblox')
            st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
            options3 = st.radio('Question 3',['Roblox','Builderman'])
        
        if st.sidebar.button('Submit'):
            pass

#quiztable = {'Username':[username],'Score':[score]}
#st.table(quiztable)

#st.table(quizscore)



