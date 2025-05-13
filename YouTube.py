import streamlit as st
import webbrowser
import pandas as pd

st.set_page_config(page_title='YouTube Pig',page_icon='🐷')

menu = st.sidebar.selectbox('Menu',['Video Categories','Video Ratings'])

try:
    import plotly_express as px
except:
    st.error('')

try:
    videolink = pd.read_csv('videorating.csv')
except:
    videolink = pd.DataFrame()

st.title('YouTube 🐷')

st.write('')#spacer

if menu == 'Video Categories':
    videocat = st.sidebar.radio('Choose Videos',['All','Gaming','Sports','Construction','Kids'])

    if videocat == 'All' or videocat == 'Gaming':
        st.subheader('Gaming')

        gm1,gm2,gm3,gm4 = st.columns(4)

        with gm1:
            st.image('https://i.ytimg.com/vi/iAoZFghpRzY/maxresdefault.jpg')
            st.write('Roblox Video Game Tycoon')
            st.success('23:56')
            if st.button(label='Play Video',key='1'):
                webbrowser.open('https://www.youtube.com/watch?v=iAoZFghpRzY')
                try:
                    videolink.loc[0,'Roblox Video Game Tycoon'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Roblox Video Game Tycoon'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/X5hsmqElIME/maxresdefault.jpg')
            st.write('Roblox Piggy Book 1')
            st.success('4:53:55')
            if st.button(label='Play Video',key='2'):
                webbrowser.open('https://www.youtube.com/watch?v=X5hsmqElIME')
                try:
                    videolink.loc[0,'Roblox Piggy Book 1'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Roblox Piggy Book 1'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with gm2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvMc0wZJklMriLs_P3jPqeU9hjY2KIN_TfHQ&s')
            st.write('Minecraft Gameplay Walkthrough Full Game')
            st.success('11:40:04')
            if st.button(label='Play Video',key='3'):
                webbrowser.open('https://www.youtube.com/watch?v=mxHIFijxTZY')
                try:
                    videolink.loc[0,'Minecraft Gameplay Walkthrough Full Game'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Minecraft Gameplay Walkthrough Full Game'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmIj4APxj-Eb_WanUAjhG0PbHDCjkuQAfelw&s')
            st.write('Roblox Piggy Book 2')
            st.success('2:05:35')
            if st.button(label='Play Video',key='4'):
                webbrowser.open('https://www.youtube.com/watch?v=Qil2bO3zG3')
                try:
                    videolink.loc[0,'Roblox Piggy Book 2'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Roblox Piggy Book 2'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with gm3:
            st.image('https://i.ytimg.com/vi/lbk3Yie7_0I/maxresdefault.jpg')
            st.write('Fortnite is MEGA (Season Reaction)')
            st.success('15:38')
            if st.button(label='Play Video',key='5'):
                webbrowser.open('https://www.youtube.com/watch?v=lbk3Yie7_0I')
                try:
                    videolink.loc[0,'Fortnite is MEGA (Season Reaction)'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Fortnite is MEGA (Season Reaction)'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/58FeoJdNLKo/maxresdefault.jpg')
            st.write('Minecraft 100 Days')
            st.success('18:02')
            if st.button(label='Play Video',key='6'):
                webbrowser.open('https://www.youtube.com/watch?v=58FeoJdNLKo')
                try:
                    videolink.loc[0,'Minecraft 100 Days'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Minecraft 100 Days'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with gm4:
            st.image('https://i.ytimg.com/vi/tBfeIXLuOYg/maxresdefault.jpg')
            st.write('Minecraft But Every 10 Seconds TNT Spawns')
            st.success('23:46')
            if st.button(label='Play Video',key='7'):
                webbrowser.open('https://www.youtube.com/watch?v=tBfeIXLuOYg')
                try:
                    videolink.loc[0,'Minecraft But Every 10 Seconds TNT Spawns'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Minecraft But Every 10 Seconds TNT Spawns'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/yDt87mPmBlQ/maxresdefault.jpg')
            st.write('Realistic Minecraft')
            st.success('18:08')
            if st.button(label='Play Video',key='8'):
                webbrowser.open('https://www.youtube.com/watch?v=yDt87mPmBlQ')
                try:
                    videolink.loc[0,'Realistic Minecraft'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Realistic Minecraft'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        st.subheader('')#spacer

    if videocat == 'All' or videocat == 'Sports':
        st.subheader('Sports')

        sp1,sp2,sp3,sp4 = st.columns(4)

        with sp1:
            st.image('https://i.ytimg.com/vi/Qqj-ImDsYk8/maxresdefault.jpg')
            st.write('Rocket League Story Mode')
            st.success('32:14')
            if st.button(label='Play Video',key='9'):
                webbrowser.open('https://www.youtube.com/watch?v=Qqj-ImDsYk8')
                try:
                    videolink.loc[0,'Rocket League Story Mode'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Rocket League Story Mode'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/eU6ouVA3dRc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBmSuVWq0TUrkN1mab6A5CmTjs_lA')
            st.write('Winning Every Rocket League Game in a Row')
            st.success('36:47')
            if st.button(label='Play Video',key='10'):
                webbrowser.open('https://www.youtube.com/watch?v=eU6ouVA3dRc')
                try:
                    videolink.loc[0,'Winning Every Rocket League Game in a Row'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Winning Every Rocket League Game in a Row'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with sp2:
            st.image('https://images2.minutemediacdn.com/image/upload/c_crop,w_3838,h_2158,x_0,y_0/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/images/voltaxMediaLibrary/mmsport/esports_illustrated/01j4hzxrkt5rzvzcrkkn.jpg')
            st.write('EAFC 25 Mobile Gameplay')
            st.success('9:22')
            if st.button(label='Play Video',key='11'):
                webbrowser.open('https://www.youtube.com/watch?v=ZnHrAuK5e60')
                try:
                    videolink.loc[0,'EAFC 25 Mobile Gameplay'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'EAFC 25 Mobile Gameplay'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/eC6aM_Eef1U/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLA-mJK86wq7dotffJcTrh_Yh5lK2Q')
            st.write('The FC 25 Gamplay is actually GOOD')
            st.success('10:21')
            if st.button(label='Play Video',key='12'):
                webbrowser.open('https://www.youtube.com/watch?v=eC6aM_Eef1U')
                try:
                    videolink.loc[0,'The FC 25 Gamplay is actually GOOD'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'The FC 25 Gamplay is actually GOOD'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with sp3:
            st.image('https://cdn.mos.cms.futurecdn.net/rHSFRBAvLiXw2obQr53nh5.jpg')
            st.write('HIGHLIGHTS | Arsenal vs Man City')
            st.success('2:17')
            if st.button(label='Play Video',key='13'):
                webbrowser.open('https://www.youtube.com/watch?v=4-H15-CeFQo')
                try:
                    videolink.loc[0,'HIGHLIGHTS | Arsenal vs Man City'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'HIGHLIGHTS | Arsenal vs Man City'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/UcnB9e5O5NY/maxresdefault.jpg')
            st.write('The Ultimate Guide for Shooting a Basketball')
            st.success('6:20')
            if st.button(label='Play Video',key='14'):
                webbrowser.open('https://www.youtube.com/watch?v=UcnB9e5O5NY')
                try:
                    videolink.loc[0,'The Ultimate Guide for Shooting a Basketball'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'The Ultimate Guide for Shooting a Basketball'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with sp4:
            st.image('https://i.ytimg.com/vi/XLH9ww29C1E/maxresdefault.jpg')
            st.write('Learn How to Dribble Better in 1 Day')
            st.success('7:55')
            if st.button(label='Play Video',key='15'):
                webbrowser.open('https://www.youtube.com/watch?v=XLH9ww29C1E')
                try:
                    videolink.loc[0,'Learn How to Dribble Better in 1 Day'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Learn How to Dribble Better in 1 Day'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/CMQp0bwjokw/maxresdefault.jpg')
            st.write('How To Dribble A Basketball')
            st.success('9:32')
            if st.button(label='Play Video',key='16'):
                webbrowser.open('https://www.youtube.com/watch?v=CMQp0bwjokw')
                try:
                    videolink.loc[0,'How To Dribble A Basketball'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'How To Dribble A Basketball'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        st.subheader('')#spacer

    if videocat == 'All' or videocat == 'Construction':
        st.subheader('Construction')

        cu1,cu2,cu3,cu4 = st.columns(4)

        with cu1:
            st.image('https://i.ytimg.com/vi/6iN78oUhB8M/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLC2cC_jge-Isd05IDtzTni3LT0g_g')
            st.write('I Built Bikini Bottom in My Backyard')
            st.success('8:06')
            if st.button(label='Play Video',key='17'):
                webbrowser.open('https://www.youtube.com/watch?v=d748kQzHuRM')
                try:
                    videolink.loc[0,'I Built Bikini Bottom in My Backyard'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built Bikini Bottom in My Backyard'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/SJN903kCJrc/maxresdefault.jpg')
            st.write('I Built a Secret Gaming Room!')
            st.success('8:59')
            if st.button(label='Play Video',key='18'):
                webbrowser.open('https://www.youtube.com/watch?v=SJN903kCJrc')
                try:
                    videolink.loc[0,'I Built a Secret Gaming Room!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built a Secret Gaming Room!'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with cu2:
            st.image('https://i.ytimg.com/vi/bfONXX3WtT4/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLD6xvTyIsiv_9Z3nHNqd_3OGMwERQ')
            st.write('I Built 5 SECRET Rooms You’d Never Find!')
            st.success('19:18')
            if st.button(label='Play Video',key='19'):
                webbrowser.open('https://www.youtube.com/watch?v=bfONXX3WtT4')
                try:
                    videolink.loc[0,'I Built 5 SECRET Rooms You’d Never Find!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built 5 SECRET Rooms You’d Never Find!'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/llAf-w1WE0c/maxresdefault.jpg')
            st.write('I Built The Krusty Krab in Real Life!')
            st.success('8:41')
            if st.button(label='Play Video',key='20'):
                webbrowser.open('https://www.youtube.com/watch?v=llAf-w1WE0c')
                try:
                    videolink.loc[0,'I Built The Krusty Krab in Real Life!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built The Krusty Krab in Real Life!'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with cu3:
            st.image('https://s1.cdn.autoevolution.com/images/news/gallery/this-luxury-tiny-house-costs-only-25000-and-is-towed-by-a-cybertruck_20.jpg')
            st.write('I Built a Luxury $25,000 Tiny House!')
            st.success('16:57')
            if st.button(label='Play Video',key='21'):
                webbrowser.open('https://www.youtube.com/watch?v=Xwc4VqF6y1U')
                try:
                    videolink.loc[0,'I Built a Luxury $25,000 Tiny House!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built a Luxury $25,000 Tiny House!'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/4PHGAPMdrAo/maxresdefault.jpg')
            st.write('I Built a Real Life Fortnite Battle Bus!')
            st.success('8:10')
            if st.button(label='Play Video',key='22'):
                webbrowser.open('https://www.youtube.com/watch?v=4PHGAPMdrAo')
                try:
                    videolink.loc[0,'I Built a Real Life Fortnite Battle Bus!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built a Real Life Fortnite Battle Bus!'] = 1
                    videolink.to_csv('videorating.csv',index=False)

        with cu4:
            st.image('https://i.ytimg.com/vi/VQq0gQvKJmM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBiDOvmynBjcSnKgBgGRO_JveuJFA')
            st.write('I Built My House out of Legos')
            st.success('13:33')
            if st.button(label='Play Video',key='23'):
                webbrowser.open('https://www.youtube.com/watch?v=VQq0gQvKJmM')
                try:
                    videolink.loc[0,'I Built My House out of Legos'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built My House out of Legos'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/eguZ2NHXWsM/maxresdefault.jpg')
            st.write('I Built MrBeast a Real Life Fortnite Battle Bus!')
            st.success('9:45')
            if st.button(label='Play Video',key='24'):
                webbrowser.open('https://www.youtube.com/watch?v=eguZ2NHXWsM')
                try:
                    videolink.loc[0,'I Built MrBeast a Real Life Fortnite Battle Bus!'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'I Built MrBeast a Real Life Fortnite Battle Bus!'] = 1
                    videolink.to_csv('videorating.csv',index=False)

        st.subheader('')
        
    if videocat == 'All' or videocat == 'Kids':
        st.subheader('Kids')
        st.write('For Ages 5 and below')

        k1,k2,k3,k4 = st.columns(4)

        with k1:
            st.image('https://upload.wikimedia.org/wikipedia/en/thumb/8/86/Peppa_Pig_logo.svg/1200px-Peppa_Pig_logo.svg.png')
            st.write('Peppa Pig')
            st.success('1:04:06')
            if st.button(label='Play Video',key='25'):
                webbrowser.open('https://www.youtube.com/watch?v=Ur--7Y1odjM')
                try:
                    videolink.loc[0,'Peppa Pig'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Peppa Pig'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://cdn.shopify.com/s/files/1/0899/1470/files/IMG_1465sm.jpg?v=1678441228')
            st.write('Peppa Pig')
            st.success('2:05:34')
            if st.button(label='Play Video',key='26'):
                webbrowser.open('https://www.youtube.com/watch?v=XHB1w51V02A')
                try:
                    videolink.loc[0,'Peppa Pig'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Peppa Pig'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with k2:
            st.image('https://images.gem.cbc.ca/v1/synps-cbc/show/perso/cbc_pawpatrol_ott_background_v02.jpg?impolicy=ott&im=Resize=(_Size_)&quality=75')
            st.write('Paw Patrol')
            st.success('12:06')
            if st.button(label='Play Video',key='27'):
                webbrowser.open('https://www.youtube.com/watch?v=z1vXJVI2L5M')
                try:
                    videolink.loc[0,'Paw Patrol'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Paw Patrol'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://m.media-amazon.com/images/S/pv-target-images/206a456e12473cd5f5dd92e1e20015eaaded007bd74711ecfdb6937bdfea525d.jpg')
            st.write('Paw Patrol')
            st.success('1:45:59')
            if st.button(label='Play Video',key='28'):
                webbrowser.open('https://www.youtube.com/watch?v=298CQJfZsL8')
                try:
                    videolink.loc[0,'Paw Patrol'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Paw Patrol'] = 1
                    videolink.to_csv('videorating.csv',index=False)

        with k3:
            st.image('https://modernparenting-onemega.com/wp-content/uploads/2024/11/Theres-Another-Blippi-And-Heres-Why-2240x1260.jpg')
            st.write('Blippi')
            st.success('30:24')
            if st.button(label='Play Video',key='29'):
                webbrowser.open('https://www.youtube.com/watch?v=iW4HMPeU3rw')
                try:
                    videolink.loc[0,'Blippi'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Blippi'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/dLPpNMBm_3k/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLABXdqIU4P1vRghjkH1a7jb7C-f4Q')
            st.write('Blippi')
            st.success('2:05:09')
            if st.button(label='Play Video',key='30'):
                webbrowser.open('https://www.youtube.com/watch?v=dLPpNMBm_3k')
                try:
                    videolink.loc[0,'Blippi'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Blippi'] = 1
                    videolink.to_csv('videorating.csv',index=False)
        
        with k4:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAjHGf-acigke5MW6q7orJzVT7PC1eiCEcZg&s')
            st.write('Cocomelon')
            st.success('47:28')
            if st.button(label='Play Video',key='31'):
                webbrowser.open('https://www.youtube.com/watch?v=UCFxJIYgCtQ')
                try:
                    videolink.loc[0,'Cocomelon'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Cocomelon'] = 1
                    videolink.to_csv('videorating.csv',index=False)

            st.write('')

            st.image('https://i.ytimg.com/vi/oGspaEENWRM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAxbH6SY7oZU_DCRqvZ523ZZpBtzg')
            st.write('Cocomelon')
            st.success('2:00:58')
            if st.button(label='Play Video',key='32'):
                webbrowser.open('https://www.youtube.com/watch?v=1zU3fEMSOVo')
                try:
                    videolink.loc[0,'Cocomelon'] += 1
                    videolink.to_csv('videorating.csv',index=False)
                except KeyError:
                    videolink.loc[0,'Cocomelon'] = 1
                    videolink.to_csv('videorating.csv',index=False)
            

if menu == 'Video Ratings':
    try:
        #st.table(videolink)
        chart = st.radio('Chart',['Bar Chart','Pie Chart'])
        melt_table = videolink.melt(var_name='Video Title',value_name='Plays')
        if chart == 'Bar Chart':
            plotbar = px.bar(melt_table, x = 'Video Title', y = 'Plays')
            st.plotly_chart(plotbar)
        if chart == 'Pie Chart':
            piechart = px.pie(melt_table,names='Video Title',values='Plays')
            st.plotly_chart(piechart)
    except:
        st.error('')