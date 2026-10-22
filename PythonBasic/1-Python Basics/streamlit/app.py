import streamlit as st
import numpy as np
import pandas as pd 

## Title of Application

st.title("Hello streamlit")

# Display simple text

st.write("Hello World ")

#Create a simple DataFrame

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column': [10,20,30,40]
})

#Display the DateFrame 

st.write("Here is the DataFrame")
st.write(df)

## Create a Line Chart 

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)