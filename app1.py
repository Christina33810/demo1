import streamlit as st

st.title("Retail Business Dashboard")

st.header('Manager Input Section')
st.write("Please enter the monthly sales target and select the region.")

st.number_input("Enter your monthly sales target (in USD):",
                min_value=0,
                max_value=100000,
                value=500000)

