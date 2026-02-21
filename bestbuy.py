import streamlit as st
import webbrowser
import pandas as pd

st.set_page_config(page_title='Best Sell',page_icon='🏷️')

menu = st.sidebar.selectbox('Options',['Buy','Sell'])

st.title('Best Sell')

st.subheader('')

shop = st.sidebar.radio('Shop:',['All','Computers/Monitors/Laptops'])

if shop == 'Computers/Monitors/Laptops':
    if menu == 'Buy':
        st.header('Computers:')
        computer1,computer2,computer3,computer4,computer5 = st.columns(5)

        with computer1:
            st.image('https://i5.walmartimages.com/asr/8c31596c-31e8-4ea1-80b4-f1a0619c5ad9.36ebde66280a2731c4e1f49f4207d8c8.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF')
            st.write('Dell Optiplex 3060 Desktop Computer')
            st.success('$549.99')
        with computer2:
            st.image('https://i5.walmartimages.com/asr/faa4a873-7766-4739-81e8-bfa7822d7b07.6838c493d0704deccc7e9d53ccbc805d.png?odnHeight=640&odnWidth=640&odnBg=FFFFFF')
            st.write('Dell OptiPlex 7450 AIO  | Refurbished')
            st.success('$299.00')
        with computer3:
            st.image('https://i5.walmartimages.com/asr/da14cfb2-14b0-4c71-a5fa-0e1429c37e8f.11528b090b5a21fc0f99c745be5b62db.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF')
            st.write('HP EliteDesk 800 G1 SFF Computer')
            st.success('$469.99')
        with computer4:
            st.image('https://i5.walmartimages.com/asr/4b15b277-ea94-430a-8519-954f4c6af95f.c77c6350170fbf82be2b2651ac63a142.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF')
            st.write('22 inch FHD Computer')
            st.success('$427.99')
        with computer5:
            st.image('https://i5.walmartimages.com/asr/663c0bc6-f87e-464e-a587-10abc51dcd80.ddb9097c166dd2e09d1af97b2aa7cf81.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF')
            st.write('Windows 10 Pro/Home')
            st.success('$279.99')

        st.subheader('')

        st.header('Monitors:')
        monitor1,monitor2,monitor3,monitor4,monitor5 = st.columns(5)














