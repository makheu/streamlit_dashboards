import streamlit as st
import seaborn as sns

st.header("This Video is brought to you by #baba")
st.text("Are you enjoying in listening this new thing")
st.header("Dont know what to write")
st.header("checking the changes")
st.text("again checking")

df = sns.load_dataset("iris")
st.write(df[['species','sepal_length','petal_length']].head())

st.bar_chart(df["sepal_length"])
st.line_chart(df['sepal_length'])


