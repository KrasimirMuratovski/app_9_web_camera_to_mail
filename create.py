import streamlit as st
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

st.line_chart(data=df)


data = {'x':[1,2,3], 'y': [10, 20, 30]}
df = pd.DataFrame(data)

ser = pd.Series([1,2,3,4,5])
st.line_chart(data=ser)



