import streamlit as st

st.set_page_config(page_title=' Pig Calculate',page_icon='📱')

cal1,cal2 = st.columns(2)

cal = '---'

with cal1:
    num1 = st.number_input('Number 1:')

    if st.button(' Add '):
        cal = 'addition'
    if st.button(' Multiply'):
        cal = 'multiplication'

with cal2:
    num2 = st.number_input('Number 2:')

    if st.button(' Subtract '):
        cal = 'subtraction'
    if st.button(' Divide '):
        cal = 'division'

if cal == 'addition':
    total = num1 + num2
elif cal == 'subtraction':
    total = num1 - num2
elif cal == 'multiplication':
    total = num1 * num2
elif cal == 'division':
    total = num1 / num2
else:
    total = '0'


st.subheader('')#spacer


st.write('Answer:')
st.subheader(total)

st.subheader('')#spacer

math = {'Number 1':num1,'Number 2':num2,'Operator':cal,'Result':total}


st.table(math)