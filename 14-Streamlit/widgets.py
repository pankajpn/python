import streamlit as st
import pandas as pd
import numpy as np

#Title of the application
st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")

age=st.slider("Select your age:", 0,100,25)

st.write(f"Your age is {age}")

options=["Python", "Java", "C++", "JavaScript"]
choice=st.selectbox("Choose your favourite language: ", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")


df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10, 20, 30, 40, 50]
})

st.write("Here is the dataframe")
st.write(df)

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not  None:
    df=pd.read_csv(uploaded_file)
    st.write(df)