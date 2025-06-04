import streamlit as st
import pandas as pd


st.set_page_config(page_title='Pig Clicker',page_icon='🐷')

try:
    clicklink = pd.read_csv('click.csv')
except:
    clicklink = pd.DataFrame()




clickpower = 1
persecond = 0

money = 0


clicklink.loc[0,'Click Power'] =1
clicklink.to_csv('click.csv',index=False)

clicklink.loc[0,'Per Second'] =0
clicklink.to_csv('click.csv',index=False)

clicklink.loc[0,'Clicks'] =0
clicklink.to_csv('click.csv',index=False)

clicklink.loc[0,'Money'] =0
clicklink.to_csv('click.csv',index=False)




money1,money2 = st.columns(2)


st.sidebar.write('Made by Dem')



if st.sidebar.checkbox('Curser: 50🪙'):
    if money >= 50:
        clicklink.loc[0,'Money'] -50
        clicklink.to_csv('click.csv',index=False)

        clicklink.loc[0,'Click Power'] +=1
        clicklink.to_csv('click.csv',index=False)
    else:
        st.error('You cannot Purchase this clicker')

if st.sidebar.checkbox('Auto Click: 125🪙'):
    if money >= 0:
        clicklink.loc[0,'Money'] -125
        clicklink.to_csv('click.csv',index=False)

        clicklink.loc[0,'Per Second'] +=1
        clicklink.to_csv('click.csv',index=False)
        persecond +=1
    else:
        st.error('You cannot Purchase this clicker')





st.image('https://media.sketchfab.com/models/186664a59a0244b2aeaa5ead307d3667/thumbnails/d851d3fb07514932bdba554cff41a3dd/8d5f08a746854a349f6df0ebff595207.jpeg')


piggy1,piggy2 = st.columns(2)

with piggy2:
    if st.button('Click'):
        clicklink.loc[0,'Clicks'] +=1
        clicklink.to_csv('click.csv')

        clicklink.loc[0,'Money'] +=1
        clicklink.to_csv('click.csv',index=False)


if persecond > 0:
    while True:
        money +=1




with money2:
    st.title(money,'🪙')


st.table(clicklink)