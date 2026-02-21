import streamlit as st
import pandas as pd
import plotly_express as px



try:
    csvfile = pd.read_csv('medical.csv')
except:
    csvfile = pd.DataFrame()


menu = st.sidebar.selectbox('Menu',['Quiz','Results'])



st.title('Medical Awareness Quiz')

if menu == 'Quiz':

    username = st.text_input('Enter Name:',placeholder='Enter Name:',label_visibility='collapsed')
    if username:
        if st.sidebar.checkbox('Start'):
            csvfile.loc[0,username] =0
            csvfile.to_csv('medical.csv')

            quiz1,quiz2 = st.columns(2)
            with quiz1:
                options1 = st.selectbox('What is the main job of your heart?',['Choose:','Pumping blood','Digesting food','Storing energy','Breathing air'])
                options2 = st.selectbox('What do vaccines help protect you from?',['Choose:','Common cold','Diseases like measles and flu','Cuts and bruises','None of the above'])
                options3 = st.selectbox('Why is it important to wash your hands?',['Choose:','To smell nice','To prevent getting sick','To look clean','None of the above'])
                options4 = st.selectbox('What should you do if you have a fever?',['Choose:','Go play outside','Tell an adult and rest','Eat a lot of candy','Stay up late'])
                options5 = st.selectbox('What does a doctor do?',['Choose:','Fix cars','Help people stay healthy','Teach math','None of the above'])
                options6 = st.selectbox('What is a healthy snack?',['Choose:','Candy','Fruits and vegetables','Chips','Soda'])
                options7 = st.selectbox('What does it mean to be allergic to something?',['Choose:','You like it a lot','You can’t eat it','Your body reacts badly to it','None of the above'])
                options8 = st.selectbox('What should you do if you get a cut?',['Choose:','Ignore it','Wash it and put a bandage on it','Show it to your friends','None of the above'])
                options9 = st.selectbox('Why is it important to eat breakfast?',['Choose:','You can skip it','It’s the best meal of the day','It gives you energy','None of the above'])
                options10 = st.selectbox('What is one way to keep your bones strong?',['Choose:','Eating junk food','Avoiding exercise','Drinking milk or eating dairy','None of the above'])
            
            with quiz2:
                options11 = st.selectbox('What is the purpose of first aid?',['Choose:','To help with homework','To give immediate care in emergencies','To make food','None of the above'])
                options12 = st.selectbox('What can help you breathe better when you’re sick?',['Choose:','Eating ice cream','Drinking warm fluids','Eating Gum','None of the above'])
                options13 = st.selectbox('What is a common symptom of a cold?',['Choose:','Runny nose','Happy thoughts','Feeling Cold','None of the above'])
                options14 = st.selectbox('Why should you cover your mouth when you cough?',['Choose:','To look funny','To prevent spreading germs','To make a sound','None of the above'])
                options15 = st.selectbox('What is a safe way to exercise?',['Choose:','Jumping on the bed','Playing sports or riding a bike','Sitting all day','None of the above'])
                options16 = st.selectbox('What does a dentist check?',['Choose:','Your eyes','Your hair','Your teeth','None of the above'])
                options17 = st.selectbox('What should you do if you feel dizzy?',['Choose:','Keep running','Sit down and tell an adult','Eat a lot of candy','None of the above'])
                options18 = st.selectbox('What is the main function of your lungs?',['Choose:','To pump blood','To help you breathe','To digest food','None of the above'])
                options19 = st.selectbox('What can help you stay healthy during cold and flu season?',['Choose:','Washing hands frequently','Eating more sweets','Skipping sleep','None of the above'])
                options20 = st.selectbox('What does it mean if someone has a headache?',['Choose:','They are happy','They might need rest or water','They want to play','None of the above'])

            if st.sidebar.button('Submit'):
                if options1 == 'Choose:' or options2 == 'Choose:' or options3 == 'Choose:' or options4 == 'Choose:' or options5 == 'Choose:' or options6 == 'Choose:' or options7 == 'Choose:' or options8 == 'Choose:' or options9 == 'Choose:' or options10 == 'Choose:':
                    st.sidebar.error('Not all Questions has been answered')
                
                elif options11 == 'Choose:' or options12 == 'Choose:' or options13 == 'Choose:' or options14 == 'Choose:' or options15 == 'Choose:' or options16 == 'Choose:' or options17 == 'Choose:' or options18 == 'Choose:' or options19 == 'Choose:' or options20 == 'Choose:':
                    st.sidebar.error('Not all Questions has been answered')
                
                else:
                    if options1 == 'Pumping blood':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options2 == 'Diseases like measles and flu':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options3 == 'To prevent getting sick':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options4 == 'Tell an adult and rest':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options5 == 'Help people stay healthy':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options6 == 'Fruits and vegetables':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options7 == 'Your body reacts badly to it':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options8 == 'Wash it and put a bandage on it':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options9 == 'It gives you energy':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options10 == 'Drinking milk or eating dairy':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options11 == 'To give immediate care in emergencies':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options12 == 'Drinking warm fluids':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options13 == 'Runny nose':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    if options14 == 'To prevent spreading germs':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options15 == 'Playing sports or riding a bike':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options16 == 'Your teeth':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options17 == 'Sit down and tell an adult':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options18 == 'To help you breathe':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options19 == 'Washing hands frequently':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)
                    
                    if options20 == 'They might need rest or water':
                        csvfile.loc[0,username] +=10
                        csvfile.to_csv('medical.csv',index=False)

                    st.sidebar.success('Your answers had been submitted')

if menu == 'Results':
    melt_table = csvfile.melt(var_name='Username',value_name='Score')
    charts = st.sidebar.radio('Charts',['Bar Chart','Pie Chart'])
    if charts == 'Bar Chart':
        plotbar = px.bar(melt_table, x='Username',y='Score')
        st.plotly_chart(plotbar)
    
    if charts == 'Pie Chart':
        piechart = px.pie(melt_table, names='Username',values='Score')
        st.plotly_chart(piechart)



