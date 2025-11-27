import streamlit as st

st.title("Retail Business Dashboard")

st.header('Manager Input Section')
st.write("Please enter the monthly sales target and select the region.")

monthly_sales_target = st.number_input("Enter your monthly sales target (in USD):",
                                      min_value=0,
                                      max_value=1000000,
                                      value=500000)
                        
