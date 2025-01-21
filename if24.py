import streamlit as st


circuit_name = st.text_input('Name:')

voltage = st.number_input('Voltage:')

resistance = st.number_input('Resistance:')

current = voltage / resistance

if current > 15:
    st.write('Warning',circuit_name+'! Your current is',current,'amps which exceeds safe operating limits!')



