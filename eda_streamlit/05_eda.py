# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns 

# Webapp Title

st.markdown('''
 # **Exploratory Data Analysis Web Application** 
This app is developed with the Codanics Youtube Channel Collaboration called **EDA App**
''')

# How to upload a file from PC

with st.sidebar.header (" Upload Your Dataset (.csv)") :
     uploaded_file= st.sidebar.file_uploader('Upload your file', type=['csv'])
     df= sns.load_dataset('titanic')
     st.sidebar.markdown("[Example CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download)")
     
     
# profiling report for Pandas 

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv= pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr= ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write("----")
    st.header("**Profiling report with pandas**")
    st_profile_report(pr)
    
else:
    st.info('Awaiting for CSV file, upload kr b do')
    if st.button("press to use example data"):
    # example data
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                         columns=['age','banana','codanics','Deutchland','Ear'])
            return a
    df= load_data()
    pr= ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write("----")
    st.header("**Profiling report with pandas**")
    st_profile_report(pr) 
    
    
         