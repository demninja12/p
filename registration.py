import streamlit as st
import pandas as pd

st.set_page_config(page_title='School Registration',page_icon='📕')



st.header('Student Registration Form')


st.subheader('')#spacer


st.subheader('Student Information')

img1,img2 = st.columns(2)

student1,student2 = st.columns(2)

with img1:
    profile = st.file_uploader('Upload Student Image:',type=['jpg','jpeg','png'])

with img2:
    if profile:
        st.image(profile)

with student1:
    fullname = st.text_input('Full Name:')

    gender = st.radio('Gender:',['Male','Female'],horizontal=True)

    grade = st.selectbox('Grade:',['Kindergarden','Grade 1','Grade 2','Grade 3','Grade 4'])


with student2:
    dob = st.date_input('Date of Birth:')

    nationality = st.text_input('Nationality:')

    studentemail = st.text_input('Student Email:')


st.write('')#spacer
contactinfo = st.text_input('Contact Information:')


st.subheader('')#spacer


st.subheader('Parent/Guardian Information')

parent1,parent2 = st.columns(2)

with parent1:
    parentname = st.text_input('Parent/Guardian Name(s):')

    parentcontact = st.text_input('Contact Information (Phone Number, Email):')



with parent2:
    relation = st.text_input('Relation to Student:')

    emgcontact = st.text_input('Emergency Contact Information:')


st.write('')#spacer
address = st.text_input('Address:')




