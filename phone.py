import streamlit as st
import pandas as pd

st.set_page_config(page_title='Phone',page_icon='📱')

try:
    phonestat = pd.read_csv('phone.csv')
except:
    phonestat = pd.DataFrame()



phone,title = st.columns(2)



donate = st.sidebar.number_input('Donate Here:')
if st.sidebar.button('Donate',key=1):
    try:
        phonestat.loc[0,'Raised'] +=donate
        phonestat.to_csv('phone.csv',index=False)
    except:
        phonestat.loc[0,'Raised'] = donate
        phonestat.to_csv('phone.csv',index=False)

try:
    raisedstat = phonestat["Raised"].iloc[0]
except:
    pass


try:
    raised = (donate)
except:
    raised = (0)

#precent = 0
#try:
    #precent = raisedstat / 5
#except:
    #precent = 0



#try:
    #phonestat.loc[0,'Precentage'] = donate / 5
    #phonestat.loc('phone.csv',index=False)
#except:
    #phonestat.loc[0,'Precentage'] = 0
    #phonestat.to_csv('phone.csv',index=False)




with phone:
    st.image('https://m.media-amazon.com/images/I/61IqkfGCw5L.jpg')

with title:
    st.title('Samsung Galaxy Z Flip5')
    st.divider()
    st.title('Money Needed:')
    st.header('$500')

st.divider()

stats1,stats2 = st.columns(2)

with stats1:
    st.header('Raised:')
    try:
        st.subheader(raisedstat)
    except:
        st.subheader('0')

with stats2:
    st.header('Precentage:')
    try:
        precent = (int(raisedstat / 5))
        st.subheader(precent)
    except:
        st.subheader('0%')

st.divider()


