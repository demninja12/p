import streamlit as st


uploadimage = st.file_uploader('Upload file',['jpg','jpeg','png'])

if uploadimage:
    st.image(uploadimage)
    with open('changeimage.png', 'wb') as writeimage:
        writeimage.write(uploadimage.getbuffer())
        st.success('Image Saved')