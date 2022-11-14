import streamlit as st
import seaborn as sns 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# making containers 
header=st.container()
data_sets=st.container()
features=st.container()
model_training=st.container()

with header:
    st.title('Kashti Dataset App')
    st.text('In this project we shall work on the Kashti data')
    
with data_sets:
    st.header("Kashti drowned.!, oh No :(")
    st.text("We shall work on the titanic data sets")
    df= sns.load_dataset("titanic")
    # removing NAN values
    df= df.dropna()
    st.write(df.head(10))
    st.subheader("Gender")
    st.bar_chart(df['sex'].value_counts())
    # drawing other plots
    st.subheader("Class Difference")
    st.bar_chart(df['class'].value_counts())
    #Barplot
    st.bar_chart(df['age'].sample(10)) # or head()
    st.markdown('1. **Feature 1:** This will tell us details')

    
with features:
    st.header("these are our App features")
    st.text("We shall add various features, but later on...")
    
with model_training:
    st.header("What happened to Kashti model training")
    st.text("We shall add/reduce various parameters")
    # Making Columns
    input, display = st.columns(2)
    # we need to choose selection points for columns
    max_depth=input.slider('how many people do you know', min_value=10, max_value=200, step=5)
    # In random forests there are n estimators 
n_estimators = input.selectbox('How many trees should be there in the Random Forest RF?', options=[50,100,150,200,250,300, 'NO limit'])

# adding list of features
input.write(df.columns)
    # input features from the user
input_features= input.text_input('Which Feature we should use?')
    
# Machine Learning model

model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
# here we shall use a condition
if n_estimators == 'NO limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# definining input and output X and y

X=df[[input_features]]
y=df[['fare']]
# fit our model
model.fit(X,y)
pred= model.predict(y)    

# display metrics 

display.subheader('Mean absolute error of the model is:')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean squared error of the model is:')
display.write(mean_squared_error(y, pred))
display.subheader('R square of the model is:')
display.write(r2_score(y, pred))