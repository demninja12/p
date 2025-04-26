import streamlit as st
import pandas as pd


st.set_page_config(page_title='School Registration',page_icon='📕')


menu = st.sidebar.selectbox('Menu',['Register Student','Find Student'])


try:
    csvfile = pd.read_csv('registration.csv')
except:
    csvfile = pd.DataFrame()


studentid = 'Student'+ str(len(csvfile) + 1)

if menu == 'Register Student':


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



    if st.button('Save Student Information'):
        registrationdict = {'StudentID':[studentid],'Full Name':[fullname],'Gender':[gender],
                            'Grade':[grade],'Date of Birth':[dob],'Nationality':[nationality],
                            'Email':[studentemail],'Contact Information':[contactinfo],'Parent/Guardian Name(s)':[parentname],
                            'Parent Contact Information':[parentcontact],'Relation':[relation],
                            'Address':[address],'Emergency Contact Information':[emgcontact]}
        registrationtable = pd.DataFrame(registrationdict)
        tablesjoin = pd.concat([csvfile,registrationtable],ignore_index=True)
        tablesjoin.to_csv('registration.csv',index=False)
        #st.table(registrationtable)
        st.success('Student Information Saved')




if menu == 'Find Student':
    adminpass = '12345Dem'
    username = st.sidebar.text_input("Enter Student ID")
    loginpass = st.sidebar.text_input("Enter School Admin Pass",type='password')
    if st.sidebar.button('Find Student'):
        if loginpass == adminpass:
            if username:
                try:
                    searchuser = csvfile[csvfile['StudentID'].str.lower() == username.lower()]
                    #st.table(searchuser)
                    getid = searchuser['StudentID'].iloc[0]
                    getfn = searchuser['Full Name'].iloc[0]
                    getgend = searchuser['Gender'].iloc[0]
                    getgrd = searchuser['Grade'].iloc[0]
                    getdob = searchuser['Date of Birth'].iloc[0]
                    getnation = searchuser['Nationality'].iloc[0]
                    geteml = searchuser['Email'].iloc[0]
                    getcontinfo = searchuser['Contact Information'].iloc[0]
                    getparname = searchuser['Parent/Guardian Name(s)'].iloc[0]
                    getpci = searchuser['Parent Contact Information'].iloc[0]
                    getrel = searchuser['Relation'].iloc[0]
                    getaddr = searchuser['Address'].iloc[0]
                    getemg = searchuser['Emergency Contact Information'].iloc[0]

                    info1,info2 = st.columns(2)
                    with info1:
                        st.header(getfn)
                        st.divider()
                        st.subheader('Student Information:')
                        st.divider()
                        st.subheader('Gender:')
                        st.write(getgend)
                        st.subheader('Date of Birth:')
                        st.write(getdob)
                        st.subheader('Nationality:')
                        st.write(getnation)
                        st.subheader('Student Email:')
                        st.write(geteml)
                        st.subheader('Contact Information:')
                        st.write(getcontinfo)
                    
                    with info2:
                        st.header(getgrd)
                        st.divider()
                        st.subheader('Parent Information:')
                        st.divider()
                        st.subheader('Parent/Guardian Name(s):')
                        st.write(getparname)
                        st.subheader('Parent Contact:')
                        st.write(getpci)
                        st.subheader('Relation:')
                        st.write(getrel)
                        st.subheader('Address:')
                        st.write(getaddr)
                        st.subheader('Emergency Contact:')
                        st.write(getemg)
                    
                except:
                    st.error('')