import streamlit as st
import pandas as pd

st.set_page_config(page_title='Quiz',page_icon='❓')

try:
    import plotly_express as px
except:
    st.write('')

try:
    quizscore = pd.read_csv('quiz.csv')
except:
    quizscore = pd.DataFrame()



st.title('Roblox Quiz')

q1 =0
q2 =0
q3 =0
q4 =0
q5 =0

score = 0


points = 0

menu = st.sidebar.selectbox('Menu',['Quiz','Leaderboard'],label_visibility='collapsed')


if menu == 'Quiz':


    username = st.text_input('Enter Username:',placeholder='Enter Username:',label_visibility='collapsed')
    if username:
        if st.sidebar.checkbox('Start Quiz'):
            st.sidebar.write('Made by Dem')

            
            level = st.sidebar.radio('Difficulty',['Easy','Medium','Hard','X-Treme','Impossible'])




            if level == 'Easy':
                    easy1,easy2 = st.columns(2)

                #points = q1 + q2 + q3 + q4 + q5


                    with easy1:
                        st.subheader('Who is the Creator of Roblox')
                        st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                        options1 = st.radio('Question 1',['Jimmy Donaldson','David Baszucki','Elon Musk','Anthony Russo'],horizontal=True,label_visibility='collapsed')
                        #if st.checkbox('Submit',key=1):
                                #if options1 == 'David Baszucki':
                                    #q1 = 5
                                    #try:
                                        #quizscore.loc[0,'Score'] +=5
                                        #quizscore.to_csv('quiz.csv',index=False)
                                    #except:
                                        #quizscore.loc[0,'Score'] =5
                                        #quizscore.to_csv('quiz.csv',index=False)


                        
                        st.subheader('When was Roblox Created')
                        st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                        options2 = st.radio('Question 2',['2000','2002','2004','2006'],horizontal=True,label_visibility='collapsed')
                        #if st.checkbox('Submit',key=2):
                            #if options2 == '2006':
                                    #q2 = 5
                                    #try:
                                        #quizscore.loc[0,'Score'] +=5
                                        #quizscore.to_csv('quiz.csv',index=False)
                                    #except:
                                        #quizscore.loc[0,'Score'] =5
                                        #quizscore.to_csv('quiz.csv',index=False)
                

                        st.subheader('')#spacer

                    with easy2:
                        st.subheader('Who was the First Player on Roblox')
                        st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                        options3 = st.radio('Question 3',['Roblox','Builderman','John Doe','Jane Doe'],horizontal=True,label_visibility='collapsed')
                        #if st.checkbox('Submit',key=3):
                            #if options3 == 'Roblox':
                                    #q3 = 5
                                    #try:
                                        #quizscore.loc[0,'Score'] +=5
                                        #quizscore.to_csv('quiz.csv',index=False)
                                    #except:
                                        #quizscore.loc[0,'Score'] =5
                                        #quizscore.to_csv('quiz.csv',index=False)



                        st.subheader('What is the Roblox Currency')
                        st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                        options4 = st.radio('Question 4',['Bobux','VBucks','Tix','Robux'],horizontal=True,label_visibility='collapsed')
                        #if st.checkbox('Submit',key=4):
                            #if options4 == 'Robux':
                                    #q4 = 5
                                    #try:
                                        #quizscore.loc[0,'Score'] +=5
                                        #quizscore.to_csv('quiz.csv',index=False)
                                    #except:
                                        #quizscore.loc[0,'Score'] =5
                                        #quizscore.to_csv('quiz.csv',index=False)
                

                        st.subheader('')#spacer

                    st.subheader('What is used to Make Roblox Games')
                    st.image('https://cms-media.roblox.com/resize=width:480,fit:max/ykLvjTBYRKSdcs8DSmft')
                    options5 = st.radio('Question 5',['Roblox Creator','Roblox Hub','Roblox Studio','None of the aboves'],horizontal=True,label_visibility='collapsed')
                    #if st.checkbox('Submit',key=5):
                        #if options5 == 'Roblox Studio':
                                #q5 = 5
                                #try:
                                    #quizscore.loc[0,'Score'] +=5
                                    #quizscore.to_csv('quiz.csv',index=False)
                                #except:
                                    #quizscore.loc[0,'Score'] =5
                                    #quizscore.to_csv('quiz.csv',index=False)



                    if st.sidebar.button('Submit',key=1):
                        #points = q1 + q2 + q3 + q4 + q5
                        quizscore.loc[0,username] =0
                        quizscore.to_csv('quiz.csv',index=False)
                        #if level == 'Easy':
                            #if options1 or options2 or options3 or options4 or options5 == 'Choose':
                                #st.sidebar.error('Not all Questions have been Answered')
                        
                            #else:

                        if options1 == 'David Baszucki':
                                        quizscore.loc[0,username] +=5
                                        quizscore.to_csv('quiz.csv',index=False)

                        if options2 == '2006':
                                        quizscore.loc[0,username] +=5
                                        quizscore.to_csv('quiz.csv',index=False)
                                
                        if options3 == 'Roblox':
                                        quizscore.loc[0,username] +=5
                                        quizscore.to_csv('quiz.csv',index=False)
                                
                        if options4 == 'Robux':
                                        quizscore.loc[0,username] +=5
                                        quizscore.to_csv('quiz.csv',index=False)
                                
                        if options5 == 'Roblox Studio':
                                        quizscore.loc[0,username] +=5
                                        quizscore.to_csv('quiz.csv',index=False)
                        st.sidebar.table(quizscore)




            if level == 'Medium':
                medium1,medium2 = st.columns(2)

                with medium1:
                    st.subheader('Whats the Roblox Friend Limit')
                    st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                    options6 = st.radio('Question 6',['200','500','1000','No Limit'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=6):
                        #if options6 == '1000':
                            #try:
                                #quizscore.loc[0,'Score'] +=10
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =10
                                #quizscore.to_csv('quiz.csv',index=False)
                

                    st.subheader('How many Players are there on Roblox')
                    st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                    options7 = st.radio('Question 7',['20M','40M','60M','90M+'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=7):
                        #if options7 == '90M+':
                            #try:
                                #quizscore.loc[0,'Score'] +=10
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =10
                                #quizscore.to_csv('quiz.csv',index=False)
                
                with medium2:
                    st.subheader('What was the First Game to Reach 1 Billion Visits')
                    st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                    options8 = st.radio('Question 8',['Adopt Me','Piggy','Meep City','Blox Fruits'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=8):
                        #if options8 == 'Meep City':
                            #try:
                                #quizscore.loc[0,'Score'] +=10
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =10
                                #quizscore.to_csv('quiz.csv',index=False)
                

                    st.subheader('How many Games are there in Roblox')
                    st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                    options9 = st.radio('Question 9',['90K-','100K - 900K','10M - 30M','40M+'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=9):
                        #if options9 == '40M+':
                            #try:
                                #quizscore.loc[0,'Score'] +=10
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =10
                                #quizscore.to_csv('quiz.csv',index=False)

                
                st.subheader('Who is the Creator of Piggy')
                st.image('https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/4/c/a/4cabe4ab181df8c3ccc12716e159a8ddc33898d9_2_690x230.png')
                options10 = st.radio('Question 10',['Mitoon','Telenthric','Tinytoon','Minitoon'],horizontal=True,label_visibility='collapsed')
                #if st.button('Submit',key=10):
                    #if options10 == 'Minitoon':
                        #try:
                            #quizscore.loc[0,'Score'] +=10
                            #quizscore.to_csv('quiz.csv',index=False)
                        #except:
                            #quizscore.loc[0,'Score'] =10
                            #quizscore.to_csv('quiz.csv',index=False)
                
                if st.sidebar.button('Submit',key=2):
                        #points = q1 + q2 + q3 + q4 + q5
                        quizscore.loc[0,username] =0
                        quizscore.to_csv('quiz.csv',index=False)
                        #if level == 'Medium':
                            #if options6 or options7 or options8 or options9 or options10 == 'Choose':
                                #st.sidebar.error('Not all Questions have been Answered')
                            
                            #else:

                        if options6 == '1000':
                                            quizscore.loc[0,username] +=10
                                            quizscore.to_csv('quiz.csv',index=False)

                        if options7 == '90M+':
                                            quizscore.loc[0,username] +=10
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options8 == 'Meep City':
                                            quizscore.loc[0,username] +=10
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options9 == '40M+':
                                            quizscore.loc[0,username] +=10
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options10 == 'Minitoon':
                                            quizscore.loc[0,username] +=10
                                            quizscore.to_csv('quiz.csv',index=False)
                        st.sidebar.table(quizscore)




            if level == 'Hard':
                    
                hard1,hard2 = st.columns(2)

                with hard1:
                    st.subheader('Roblox has more than 10 Million User made games')
                    st.image('https://w0.peakpx.com/wallpaper/112/283/HD-wallpaper-roblox-red-logo-red-brickwall-roblox-logo-online-games-roblox-neon-logo-roblox-thumbnail.jpg')
                    options11 = st.radio('Question 11',['True','False'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=11):
                        #if options11 == 'True':
                            #try:
                                #quizscore.loc[0,'Score'] +=15
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =15
                                #quizscore.to_csv('quiz.csv',index=False)



                    st.subheader('Roblox used to be called GoBlocks')
                    st.image('https://w0.peakpx.com/wallpaper/112/283/HD-wallpaper-roblox-red-logo-red-brickwall-roblox-logo-online-games-roblox-neon-logo-roblox-thumbnail.jpg')
                    options12 = st.radio('Question 12',['True','False'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=12):
                        #if options12 == 'False':
                            #try:
                                #quizscore.loc[0,'Score'] +=15
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.lox[0,'Score'] =15
                                #quizscore.to_csv('quiz.csv',index=False)


                with hard2:
                    st.subheader('What was the Original Name of Roblox')
                    st.image('https://w0.peakpx.com/wallpaper/112/283/HD-wallpaper-roblox-red-logo-red-brickwall-roblox-logo-online-games-roblox-neon-logo-roblox-thumbnail.jpg')
                    options13 = st.radio('Question 13',['ImaginEngine','DynaBlocks','BloxMaker','GoBlox'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=13):
                        #if options13 == 'DynaBlocks':
                            #try:
                                #quizscore.loc[0,'Score'] +=15
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =15
                                #quizscore.to_csv('quiz.csv',index=False)



                    st.subheader('In the Past you could put Spaces in your username')
                    st.image('https://w0.peakpx.com/wallpaper/112/283/HD-wallpaper-roblox-red-logo-red-brickwall-roblox-logo-online-games-roblox-neon-logo-roblox-thumbnail.jpg')
                    options14 = st.radio('Question 14',['True','False'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=14):
                        #if options14 == 'False':
                            #try:
                                #quizscore.loc[0,'Score'] +=15
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =15
                                #quizscore.to_csv('quiz.csv',index=False)
                

                st.subheader('How many currencies has Roblox ever had')
                st.image('https://w0.peakpx.com/wallpaper/112/283/HD-wallpaper-roblox-red-logo-red-brickwall-roblox-logo-online-games-roblox-neon-logo-roblox-thumbnail.jpg')
                options15 = st.radio('Question 15',['1','2','3','4'],horizontal=True,label_visibility='collapsed')
                #if st.button('Submit',key=15):
                    #if options15 == '3':
                        #try:
                            #quizscore.loc[0,'Score'] +=15
                            #quizscore.to_csv('quiz.csv',index=False)
                        #except:
                            #quizscore.loc[0,'Score'] =15
                            #quizscore.to_csv('quiz.csv',index=False)


                
                if st.sidebar.button('Submit',key=3):
                      #points = q1 + q2 + q3 + q4 + q5
                        quizscore.loc[0,username] =0
                        quizscore.to_csv('quiz.csv',index=False)
                            
                            #else:

                        if options11 == 'True':
                                            quizscore.loc[0,username] +=15
                                            quizscore.to_csv('quiz.csv',index=False)

                        if options12 == 'False':
                                            quizscore.loc[0,username] +=15
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options13 == 'DynaBlocks':
                                            quizscore.loc[0,username] +=15
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options14 == 'False':
                                            quizscore.loc[0,username] +=15
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options15 == '3':
                                            quizscore.loc[0,username] +=15
                                            quizscore.to_csv('quiz.csv',index=False)
                        st.sidebar.table(quizscore)
            



            if level == 'X-Treme':


                x1,x2 = st.columns(2)

                with x1:
                    st.subheader('What was the First Ever Roblox Currency called')
                    st.image('https://wallpapers.com/images/hd/roblox-logo-gtm4wouo6frcras0.jpg')
                    options16 = st.radio('Question 16',['Robux','Tix','Roblox Points','None of the Aboves'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=16):
                        #if options16 == 'Roblox Points':
                            #try:
                                #quizscore.loc[0,'Score'] +=20
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =20
                                #quizscore.to_csv('quiz.csv',index=False)
                

                    st.subheader('How much Robux is the Headless Horsemen')
                    st.image('https://wallpapers.com/images/hd/roblox-logo-gtm4wouo6frcras0.jpg')
                    options17 = st.radio('Question 17',['11K','21K','31K','41K'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=17):
                        #if options17 == '31K':
                            #try:
                                #quizscore.loc[0,'Score'] +=20
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =20
                                #quizscore.to_csv('quiz.csv',index=False)
                
                with x2:
                    st.subheader('Which one is a FAKE accessory')
                    st.image('https://wallpapers.com/images/hd/roblox-logo-gtm4wouo6frcras0.jpg')
                    options18 = st.radio('Question 18',['Dire Dominus','Dominus Infernus','Dominus Empurus','Frozen Dominus'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=18):
                        #if options18 == 'Frozen Dominus':
                            #try:
                                #quizscore.loc[0,'Score'] +=20
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =20
                                #quizscore.to_csv('quiz.csv',index=False)
                

                    st.subheader('What was the Original name of Blox Fruits')
                    st.image('https://wallpapers.com/images/hd/roblox-logo-gtm4wouo6frcras0.jpg')
                    options19 = st.radio('Question 19',['One Blox','Blox Piece','Bloxy Fruits','None of the aboves'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=19):
                        #if options19 == 'Blox Piece':
                            #try:
                                #quizscore.loc[0,'Score'] +=20
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =20
                                #quizscore.to_csv('quiz.csv',index=False)
                

                st.subheader('Which one is not a Blox Fruit')
                st.image('https://wallpapers.com/images/hd/roblox-logo-gtm4wouo6frcras0.jpg')
                options20 = st.radio('Question 20',['Blizzard','Eagle','Barrier','Rubber'],horizontal=True,label_visibility='collapsed')
                #if st.button('Submit',key=20):
                    #if options20 == 'Barrier':
                        #try:
                            #quizscore.loc[0,'Score'] +=20
                            #quizscore.to_csv('quiz.csv',index=False)
                        #except:
                            #quizscore.loc[0,'Score'] =20
                            #quizscore.to_csv('quiz.csv',index=False)
                
                if st.sidebar.button('Submit',key=4):
                        #points = q1 + q2 + q3 + q4 + q5
                        quizscore.loc[0,username] =0
                        quizscore.to_csv('quiz.csv',index=False)
                            
                            #else:

                        if options16 == 'Roblox Points':
                                            quizscore.loc[0,username] +=20
                                            quizscore.to_csv('quiz.csv',index=False)

                        if options17 == '31K':
                                            quizscore.loc[0,username] +=20
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options18 == '---':
                                            quizscore.loc[0,username] +=20
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options19 == 'Blox Piece':
                                            quizscore.loc[0,username] +=20
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options20 == 'Barrier':
                                            quizscore.loc[0,username] +=20
                                            quizscore.to_csv('quiz.csv',index=False)
                        st.sidebar.table(quizscore)




            if level == 'Impossible':

                imp1,imp2 = st.columns(2)
                
                with imp1:
                    st.subheader('When was Toilet Tower Defence Created')
                    st.image('https://i.pinimg.com/736x/95/ee/e3/95eee32ca5f1395e6763cfce767e7c96.jpg')
                    options21 = st.radio('Question 21',['5/27/2023','6/17/2023','7/14/2023','4/29/2023'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=21):
                        #if options21 == '6/17/2023':
                            #try:
                                #quizscore.loc[0,'Score'] +=25
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =25
                                #quizscore.to_csv('quiz.csv',index=False)
                

                    st.subheader('When was Natural Disaster Survival Created')
                    st.image('https://i.pinimg.com/736x/95/ee/e3/95eee32ca5f1395e6763cfce767e7c96.jpg')
                    options22 = st.radio('Question 22',['4/12/2008','7/5/2009','6/9/2008','3/28/2008'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=22):
                        #if options22 == '3/28/2008':
                            #try:
                                #quizscore.loc[0,'Score'] +=25
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =25
                                #quizscore.to_csv('quiz.csv',index=False)
                
                with imp2:
                    st.subheader('When was Piggy: Intercity DEMO Created')
                    st.image('https://i.pinimg.com/736x/95/ee/e3/95eee32ca5f1395e6763cfce767e7c96.jpg')
                    options23 = st.radio('Question 23',['1/2/2021','1/22/2021','2/2/2021','2/22/2021'],horizontal=True,label_visibility='collapsed')
                    #if st.button('Submit',key=23):
                        #if options23 == '1/2/2021':
                            #try:
                                #quizscore.loc[0,'Score'] +=25
                                #quizscore.to_csv('quiz.csv',index=False)
                            #except:
                                #quizscore.loc[0,'Score'] =25
                                #quizscore.to_csv('quiz.csv',index=False)
                    

                    st.subheader('When was Break In (Story) Created')
                    st.image('https://i.pinimg.com/736x/95/ee/e3/95eee32ca5f1395e6763cfce767e7c96.jpg')
                    options24 = st.radio('Questions 24',['9/9/2019','04/03/2020','09/09/2021','01/15/2022'],horizontal=True,label_visibility='collapsed')

                    
                st.subheader('When was Tix Removed')
                st.image('https://i.pinimg.com/736x/95/ee/e3/95eee32ca5f1395e6763cfce767e7c96.jpg')
                options25 = st.radio('Questions 25',['9/6/2014','2/17/2015','4/14/2016','4/25/2018'],horizontal=True,label_visibility='collapsed')
            
                if st.sidebar.button('Submit',key=5):
                    #points = q1 + q2 + q3 + q4 + q5
                        quizscore.loc[0,username] =0
                        quizscore.to_csv('quiz.csv',index=False)
                            
                            #else:

                        if options21 == '6/17/2023':
                                            quizscore.loc[0,username] +=25
                                            quizscore.to_csv('quiz.csv',index=False)

                        if options22 == '3/28/2008':
                                            quizscore.loc[0,username] +=25
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options23 == '1/2/2021':
                                            quizscore.loc[0,username] +=25
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options24 == '9/9/2019':
                                            quizscore.loc[0,username] +=25
                                            quizscore.to_csv('quiz.csv',index=False)
                                    
                        if options25 == '64/14/2016':
                                            quizscore.loc[0,username] +=25
                                            quizscore.to_csv('quiz.csv',index=False)
                        st.sidebar.table(quizscore)





if menu == 'Leaderboard':
    st.table(quizscore)
    try:
        chart = st.sidebar.radio('Charts',['Bar Chart','Pie Chart'])
        melt_table = quizscore.melt(var_name='Username',value_name='Score')
        if chart == 'Bar Chart':
                plotbar = px.bar(melt_table, x='Username',y='Score')
                st.plotly_chart(plotbar)
        
        if chart == 'Pie Chart':
                piechart = px.pie(melt_table,names='Username',values='Score')
                st.plotly_chart(piechart)
    except:
        st.error('')





#points = q1 + q2 + q3 + q4 + q5
#quizscore.loc[0,'Score'] = points
#quizscore.to_csv('quiz.csv',index=False)
#st.sidebar.table(quizscore)






#Easy        = 5pt       /max = 25pt
#Medium      = 10pt      /max = 50pt
#Hard        = 15pt      /max = 75pt
#X-Treme     = 20pt      /max = 100pt
#Impossible  = 25pt      /max = 125pt
#total       = 75pt      /max = 375pt





        #if st.sidebar.button('Submit'):
            #st.table(quizscore)

#quiztable = {'Username':[username],'Score':[score]}
#st.table(quiztable)

#st.table(quizscore)



