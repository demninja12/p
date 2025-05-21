import streamlit as st
import pandas as pd

st.set_page_config(page_title='Quiz',page_icon='❓')

try:
    quizscore = pd.read_csv('quiz.csv')
except:
    quizscore = pd.DataFrame()

st.title('Roblox Quiz')


score = 0

username = st.text_input('Enter Username:',placeholder='Enter Username:',label_visibility='collapsed')
if st.checkbox('Start Quiz'):
    if username:
        quizscore.loc[0,'Username'] = username
        quizscore.to_csv('quiz.csv',index=False)




        level = st.sidebar.selectbox('Difficulty',['Easy','Medium','Hard','X-Treme','Impossible'])


        if level == 'Easy':

            if st.sidebar.checkbox('Question 1'):
                st.subheader('Who is the Creator of Roblox')
                st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                options1 = st.radio('Question 1',['Jimmy Donaldson','David Baszucki','Elon Musk','Anthony Russo'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=1):
                    if options1 == 'David Baszucki':
                        try:
                            quizscore.loc[0,'Score'] +=5
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =5
                            quizscore.to_csv('quiz.csv',index=False)

            if st.sidebar.checkbox('Question 2',):
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
                options3 = st.radio('Question 3',['Roblox','Builderman','John Doe','Jane Doe'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=3):
                    if options3 == 'Roblox':
                        try:
                            quizscore.loc[0,'Score'] +=5
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =5
                            quizscore.to_csv('quiz.csv',index=False)
            
            if st.sidebar.checkbox('Question 4'):
                st.subheader('What is the Roblox Currency')
                st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                options4 = st.radio('Question 4',['Bobux','VBucks','Tix','Robux'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=4):
                    if options4 == 'Robux':
                        try:
                            quizscore.loc[0,'Score'] +=5
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =5
                            quizscore.to_csv('quiz.csv',index=False)
            
            if st.sidebar.checkbox('Question 5'):
                st.subheader('What is used to Make Roblox Games')
                st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                options5 = st.radio('Question 5',['Roblox Creator','Roblox Hub','Roblox Studio','None of the aboves'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=5):
                    if options5 == 'Roblox Studio':
                        try:
                            quizscore.loc[0,'Score'] +=5
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =5
                            quizscore.to_csv('quiz.csv',index=False)




        if level == 'Medium':

            if st.sidebar.checkbox('Question 6'):
                st.subheader('Whats the Roblox Friend Limit')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options6 = st.radio('Question 6',['200','500','1000','No Limit'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=6):
                    if options6 == '1000':
                        try:
                            quizscore.loc[0,'Score'] +=10
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =10
                            quizscore.to_csv('quiz.csv',index=False)
            
            if st.sidebar.checkbox('Question 7'):
                st.subheader('How many Players are there on Roblox')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options7 = st.radio('Question 7',['20M','40M','60M','90M+'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=7):
                    if options7 == '90M+':
                        try:
                            quizscore.loc[0,'Score'] +=10
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =10
                            quizscore.to_csv('quiz.csv',index=False)
            
            if st.sidebar.checkbox('Question 8'):
                st.subheader('What was the First Game to Reach 1 Billion Visits')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options8 = st.radio('Question 8',['Adopt Me','Piggy','Meep City','Blox Fruits'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=8):
                    if options8 == 'Meep City':
                        try:
                            quizscore.loc[0,'Score'] +=10
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =10
                            quizscore.to_csv('quiz.csv',index=False)
            
            if st.sidebar.checkbox('Question 9'):
                st.subheader('How many Games are there in Roblox')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options9 = st.radio('Question 9',['90K-','100K - 900K','10M - 30M','40M+'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=9):
                    if options9 == '40M+':
                        try:
                            quizscore.loc[0,'Score'] +=10
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =10
                            quizscore.to_csv('quiz.csv',index=False)

            if st.sidebar.checkbox('Question 10'):
                st.subheader('Who is the Creator of Piggy')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options10 = st.radio('Question 10',['Mitoon','Telenthric','Tinytoon','Minitoon'],horizontal=True,label_visibility='collapsed')
                if st.button('Submit',key=10):
                    if options10 == 'Minitoon':
                        try:
                            quizscore.loc[0,'Score'] +=10
                            quizscore.to_csv('quiz.csv',index=False)
                        except:
                            quizscore.loc[0,'Score'] =10
                            quizscore.to_csv('quiz.csv',index=False)



#Easy = 5pt
#Medium = 10pt
#Hard = 15pt
#X-Treme = 20pt
#Impossible 25pt






        #if st.sidebar.button('Submit'):
            #pass

#quiztable = {'Username':[username],'Score':[score]}
#st.table(quiztable)

#st.table(quizscore)



