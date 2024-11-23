import streamlit as st    
import pandas as pd

name=st.text_input("Enter your name:")

age=st.slider("Enter your age",0,100,25)
st.write(f"Your age is {age}")

options=["C++","Java","Go","Python","C#","Javascript"]
language=st.selectbox("Select your favourite Language:",options)
st.write(f"You selected {language}.")

if name:
    st.write(f"Hello {name}")
    
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

## file uploader
uploaded_file=st.file_uploader("Choose a CSV file:",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)