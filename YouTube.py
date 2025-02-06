import streamlit as st

st.set_page_config(page_title='YouTube Pig',page_icon='🐷')

menu = st.sidebar.selectbox('Menu',['Video Categories','Video Ratings'])

st.title('YouTube 🐷')

st.write('')#spacer

if menu == 'Video Categories':
    videocat = st.sidebar.radio('Choose Videos',['All','Gaming','Sports'])

    if videocat == 'All' or videocat == 'Gaming':
        st.subheader('Gaming')

        gm1,gm2,gm3,gm4 = st.columns(4)

        with gm1:
            st.image('https://i.ytimg.com/vi/iAoZFghpRzY/maxresdefault.jpg')
            st.write('Roblox Video Game Tycoon')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=iAoZFghpRzY')

            st.write('')

            st.image('https://i.ytimg.com/vi/X5hsmqElIME/maxresdefault.jpg')
            st.write('Roblox Piggy Book 1')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=X5hsmqElIME')
        
        with gm2:
            st.image('https://i.ytimg.com/vi/6T67I2w1G2U/maxresdefault.jpg')
            st.write('Extreme $1,000,000 Minecraft Challenge')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=6T67I2w1G2U')

            st.write('')

            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmIj4APxj-Eb_WanUAjhG0PbHDCjkuQAfelw&s')
            st.write('Roblox Piggy Book 2')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=Qil2bO3zG34')
        
        with gm3:
            st.image('https://i.ytimg.com/vi/lbk3Yie7_0I/maxresdefault.jpg')
            st.write('Fortnite is MEGA (Season Reaction)')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=lbk3Yie7_0I')

            st.write('')

            st.image('https://i.ytimg.com/vi/58FeoJdNLKo/maxresdefault.jpg')
            st.write('Minecraft 100 Days')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=58FeoJdNLKo')
        
        st.subheader('')#spacer

    if videocat == 'All' or videocat == 'Sports':
        st.subheader('Sports')

        sp1,sp2,sp3,sp4 = st.columns(4)

        with sp1:
            st.image('https://i.ytimg.com/vi/EhHzJidkydo/maxresdefault.jpg')
            st.write('The Best Rocket League Game Ever!')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=EhHzJidkydo')
        
        with sp2:
            st.image('https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2195250/f11315d7491f706b09b059d12424f711e9778b82/capsule_616x353.jpg?t=1730826798')
            st.write('EAFC 24 Gameplay')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=ZnHrAuK5e60')
        
        with sp3:
            st.image('https://cdn.mos.cms.futurecdn.net/rHSFRBAvLiXw2obQr53nh5.jpg')
            st.write('HIGHLIGHTS | Arsenal vs Man City')
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=4-H15-CeFQo')