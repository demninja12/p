import streamlit as st
import pandas as pd
import plotly_express as px

try:
    vote1 = pd.read_csv('vote1.csv')
    vote2 = pd.read_csv('vote2.csv')
    vote3 = pd.read_csv('vote3.csv')
except:
    vote1 = pd.DataFrame()
    vote2 = pd.DataFrame()
    vote3 = pd.DataFrame()


st.title('Restaurant Vote')
st.header('')

vote1.loc[0,'McDonalds'] =0
vote1.to_csv('vote1.csv',index=False)

vote2.loc[0,'KFC'] =0
vote2.to_csv('vote2.csv',index=False)

vote3.loc[0,'Little Caesars'] =0
vote3.to_csv('vote3.csv',index=False)


menu = st.sidebar.selectbox('',['Vote','Leaderboard','Winners'])


if menu == 'Vote':
    option1,option2,option3 = st.columns(3)

    with option1:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMfzkUcpEmbMSQeBTh9nMkEU09OfnKL-s-4w&s')
        st.subheader('McDonalds')
        if st.button('Vote',key=1):
            vote1.loc[0,'McDonalds'] +=1
            vote1.to_csv('vote1.csv',index=False)
            st.success('Vote Success')
    
    with option2:
        st.image('https://upload.wikimedia.org/wikipedia/en/5/57/KFC_logo-image.svg')
        st.subheader('KFC')
        if st.button('Vote',key=2):
            vote2.loc[0,'KFC'] +=1
            vote2.to_csv('vote2.csv',index=False)
            st.success('Vote Success')
    
    with option3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuhfyZNyX_iV5pGt2UraT__H5ZQ3zv6sBbKQ&s')
        st.subheader('Little Caesars')
        if st.button('Vote',key=3):
            vote3.loc[0,'Little Caesars'] +=1
            vote3.to_csv('vote3.csv',index=False)
            st.success('Vote Success')



if menu == 'Leaderboard':
    st.table(vote1)
    st.table(vote2)
    st.table(vote3)
    melt_table1 = vote1.melt(var_name='McDonalds',value_name='Votes')
    st.table(melt_table1)







