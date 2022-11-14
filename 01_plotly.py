import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

st.title("Plotly and streamlit Combined App")
df = px.data.gapminder()
st.write(df)
st.write(df.head())
st.write(df.columns)


#Summary stat

st.write(df.describe())

# management of data according to the plotly 

year_option= df['year'].unique().tolist()

year=st.selectbox('which year should we plot?', year_option,0)
df= df[df['year']==year]

fig= px.scatter(df, x='gdpPercap', y='lifeExp',size='pop', color='country',hover_name='country',
                log_x=True,size_max=55,range_x=[100,100000],range_y=[20,90])
st.write(fig)


year_option= df['year'].unique().tolist()

year=st.selectbox('which year should we plot?', year_option,0)
df= df[df['year']==year]

fig= px.scatter(df, x='gdpPercap', y='lifeExp',size='pop', color='continent',hover_name='continent',
                log_x=True,size_max=55,range_x=[100,100000],range_y=[20,90])
fig.update_layout(width=1000, height=400)
st.write(fig)

