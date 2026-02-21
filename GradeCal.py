import streamlit as st


st.set_page_config(page_title='Gamer Grades',page_icon='🎮')

menu = st.sidebar.selectbox('Menu',['Submit Score'])



if menu == 'Submit Score':
    st.title('Submit Score')
    username = st.text_input('Gamer Name:',label_visibility='collapsed',placeholder='Gamer Name:')

    subject1,subject2 = st.columns(2)

    with subject1:
        st.header('Gaming:')
        st.divider()
        Roblox = st.number_input('Roblox Score:',0,100)
        Minecraft = st.number_input('Minecraft Score:',0,100)
        Fortnite = st.number_input('Fortnite Score:',0,100)

    with subject2:
        st.header('Eating:')
        st.divider()
        McDonalds = st.number_input('McDonalds Score:',0,100)
        KFC = st.number_input('KFC Score:',0,100)
        LittleCaesars = st.number_input('Little Caesars Score:',0,100)

    if st.button('Submit Score'):
        score = Roblox + Minecraft + Fortnite + McDonalds + KFC + LittleCaesars
        average = score / 6
        grade = 'ND'
        with subject1:
            st.write('Total Score:',score)
        with subject2:
            st.write('Average Score:',average)
        if average >= 100:
            grade = 'A+'
        elif average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'A-'
        
        elif average >= 75:
            grade = 'B+'
        elif average >= 70:
            grade = 'B-'
        
        elif average >= 65:
            grade = 'C+'
        elif average >= 60:
            grade = 'C-'
        
        elif average >= 55:
            grade = 'D+'
        elif average >= 50:
            grade = 'D-'
        
        else:
            grade = 'F-'

        st.sidebar.title('Grade:')
        st.sidebar.title(grade)