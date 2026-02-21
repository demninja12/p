import streamlit as st
import pandas as pd
import plotly_express as px
import webbrowser


st.set_page_config(page_title='Peggy Movie',page_icon='🎬')


try:
    csvfile = pd.read_csv('movie.csv')
except:
    csvfile = pd.DataFrame()







try:

    st.title('Peggy Movie')

    st.subheader('')


    movie1,movie2,movie3 = st.columns(3)

    menu = st.sidebar.selectbox('Movies',['All','Piggy','Poppy Playtime','Avengers'])


    play = ''
    name = ''
    moviename = ''
    movie = ''
    image = ''
    length = ''
    description = ''
    trailer = ''

    kidprice = 10
    adultprice = 13
    seniorprice = 10.25

    if menu == 'All' or menu == 'Piggy':

        st.header('Piggy')
        piggy1,piggy2,piggy3,piggy4 = st.columns(4)


        with piggy1:
            st.image('https://i.ytimg.com/vi/X5hsmqElIME/maxresdefault.jpg')
            piggyb1 = 'https://i.ytimg.com/vi/X5hsmqElIME/maxresdefault.jpg'
            if st.checkbox(label='Piggy Book 1'):
                play = 1
                moviename = 'Piggy Book 1'
                movie = 'https://www.youtube.com/watch?v=X5hsmqElIME'
                image = piggyb1
                length = '4:53:55'
                description = 'Players are trapped in various locations and must solve puzzles and find items to escape, all while being pursued by the menacing Pig.'

            if st.button(label='Watch Trailer',key=0):
                play = 2
                moviename = 'Piggy Book 1'
                trailer = 'https://www.youtube.com/watch?v=HTKCwspfsKs'



        with piggy2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmIj4APxj-Eb_WanUAjhG0PbHDCjkuQAfelw&s')
            piggyb2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmIj4APxj-Eb_WanUAjhG0PbHDCjkuQAfelw&s'
            if st.checkbox(label='Piggy Book 2'):
                play = 1
                moviename = 'Piggy Book 2'
                movie = 'https://www.youtube.com/watch?v=6JzL-7LU4CI'
                image = piggyb2
                length = '2:05:35'
                description = 'The player attempts to survive and find a cure for the infection while encountering new characters and facing moral dilemmas.'
            
            if st.button(label='Watch Trailer',key=1):
                play = 2
                moviename = 'Piggy Book 2'
                trailer = 'https://www.youtube.com/watch?v=UQkXTcmvyYE'




        with piggy3:
            st.image('https://i.ytimg.com/vi/8NbVG0k0xQ4/maxresdefault.jpg')
            piggyrp = 'https://i.ytimg.com/vi/8NbVG0k0xQ4/maxresdefault.jpg'
            if st.checkbox(label='Piggy Chapter 1-10'):
                play = 1
                moviename = 'Piggy Marathon'
                movie = 'https://www.youtube.com/watch?v=5zMSggmP864'
                image = piggyrp
                length = '1:35:15'
                description = 'This RP film delves into the story of the game Piggy, exploring the world of talking animals and the mystery surrounding a missing child named Georgie Piggy.'

            if st.button(label='Watch Trailer',key=2):
                play = 2
                moviename = 'Piggy Marathon'
                trailer = 'https://www.youtube.com/watch?v=WWWZz3HZSDQ&list=PLad-uY1_ZKbMzRCLbJSg0oPLNGVDz0P-3'
        



        with piggy4:
            st.image('https://i.ytimg.com/vi/Pj5bQSWvqgQ/mqdefault.jpg')
            antflix = 'https://i.ytimg.com/vi/Pj5bQSWvqgQ/mqdefault.jpg'
            if st.checkbox(label='Antflix'):
                play = 1
                moviename = 'Antflix'
                movie = 'https://www.youtube.com/watch?v=9Yfz8wwVJYQ&t=17s'
                image = antflix
                length = '2:21:07'
                description = 'A group of survivors in the city of Lucella try to survive an infection that turns people into monstrous creatures.'
            
            if st.button(label='Watch Trailer',key=3):
                play = 2
                moviename = 'Antflix'
                trailer = 'https://www.youtube.com/watch?v=I-Z4a7Nk6cY'
        
        st.title('')



    if menu == 'All' or menu == 'Poppy Playtime':
        
        st.header('Poppy Playtime')
        poppy1,poppy2,poppy3,poppy4 = st.columns(4)


        with poppy1:
            st.image('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1721470/capsule_616x353.jpg?t=1745345916')
            poppyplay1 = 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1721470/capsule_616x353.jpg?t=1745345916'
            if st.checkbox('Poppy Playtime 1'):
                play = 1
                moviename = 'Poppy Playtime 1'
                movie = 'https://www.youtube.com/watch?v=qLDGFudXG8I'
                image = poppyplay1
                length = '26:27'
                description = 'As an ex-employee of Playtime Co. They finally return to the factor many years after everybode within disappeared.'

            if st.button(label='Watch Trailer',key=4):
                play = 2
                moviename = 'Poppy Playtime 1'
                trailer = 'https://www.youtube.com/watch?v=xMQm8ubM-Cw'
        

        with poppy2:
            st.image('https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1817490/capsule_616x353.jpg?t=1741725727')
            poppyplay2 = 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1817490/capsule_616x353.jpg?t=1741725727'
            if st.checkbox('Poppy Playtime 2'):
                play = 1
                moviename = 'Poppy Playtime 2'
                movie = 'https://www.youtube.com/watch?v=5lsG0WHQIwk'
                image = poppyplay2
                length = '1:06:45'
                description = 'With Poppy now free, the situation begins to change rapidly while they search for any way to escape the factory'
            
            if st.button(label='Watch Trailer',key=5):
                play = 2
                moviename = 'Poppy Playtime 2'
                trailer = 'https://www.youtube.com/watch?v=XVENjm3Bjk0'
        

        with poppy3:
            st.image('https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2555190/capsule_616x353.jpg?t=1738189125')
            poppyplay3 = 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2555190/capsule_616x353.jpg?t=1738189125'
            if st.checkbox('Poppy Playtime 3'):
                play = 1
                moviename = 'Poppy Playtime 3'
                movie = 'https://www.youtube.com/watch?v=n7zbe1fpkAk'
                image = poppyplay3
                length = '3:17:43'
                description = 'In the aftermath of the train crash, they now find themself stranded in the depths with a new goal in your sigth'
            
            if st.button(label='Watch Trailer',key=6):
                play = 2
                moviename = 'Poppy Playtime 3'
                trailer = 'https://www.youtube.com/watch?v=s3_k03RC668'
        
        with poppy4:
            st.image('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3008670/f37c8d4b20246f02005c4388ea770de55386aa11/capsule_616x353.jpg?t=1738434588')
            poppyplay4 = 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3008670/f37c8d4b20246f02005c4388ea770de55386aa11/capsule_616x353.jpg?t=1738434588'
            if st.checkbox('Poppy Playtime 4'):
                play = 1
                moviename = 'Poppy Playtime 4'
                movie = 'https://www.youtube.com/watch?v=J4mfLR5J40U'
                image = poppyplay4
                length = '3:49:09'
                description = 'Further into a hell of Playtimes making, you enact Poppys plan for revenge against the Prototype.'
            
            if st.button(label='Watch Trailer',key=7):
                play = 2
                moviename = 'Poppy Playtime 4'
                trailer = 'https://www.youtube.com/watch?v=tych99G3-P0'



        
        
    if play == 1:
        with movie1:
            st.image(image)
            st.write(description)
            st.title('')
            st.title('')
            st.title('')
        
        with movie2:
            st.subheader(moviename)
            st.divider()
            if st.checkbox('Get Tickets'):
                #play = 3
                st.sidebar.title('Tickets')
                name = st.sidebar.text_input('Name',placeholder='Enter Your Name',label_visibility='collapsed')
                date = st.sidebar.date_input('Date:')
                #st.sidebar.title('')
                kids = st.sidebar.number_input('Amount of Kids (3-13):',0)
                adults = st.sidebar.number_input('Amount of Adults (14-64):',0)
                seniors = st.sidebar.number_input('Amount of Seniors (65+):',0)
                st.write('Kids: $10')
                st.write('Adults: $13')
                st.write('Seniors: $10.25')
                if st.sidebar.button('Buy Tickets'):
                    kidtotal = kidprice * kids
                    adulttotal = adultprice * adults
                    seniortotal = seniorprice * seniors
                    total = kidtotal + adulttotal + seniortotal
                    st.sidebar.subheader('Your total is:')
                    st.sidebar.subheader(total)

                    csvfile.loc[0,name] = total
                    csvfile.to_csv('movie.csv',index=False)

                    melt_table = csvfile.melt(var_name='Name',value_name='Total')

                    #st.sidebar.table(melt_table)
        
        with movie3:
            st.subheader('LENGTH:')
            st.divider()
            st.success(length)

    elif play == 2:
        with movie1:
            st.video(trailer)
            st.title('')
            st.title('')
            st.title('')
            st.title('')
        
        with movie2:
            st.subheader(moviename)
            st.divider()
            if st.button('Exit Trailer'):
                play = 0
        
    elif play == 3:
        with movie1:
            st.subheader('Tickets')
        
        with movie2:
            pass





except:
    st.sidebar.error('Something Went Wrong')