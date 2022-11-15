## Import Libraries

import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

## Page Title
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo = current_dir / "assets" / "logo.jpg"
logo = Image.open(logo)


st.image(logo, use_column_width=True)
st.write('''
# DNA Nucleotide Count Web App 
This app counts the nucleotide composition of query DNA!
***
''')

# Input Text Box
#st.sidebar.header('enter DNA sequence')
st.header("Enter DNA sequence")

sequence_input= ">DNA Query \nGATGGAACTTGACTACGTAAATT\
    sgsgsgsgsgsnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATTnGATGGAACTTGACTACGTAAATT "

# sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence= sequence.splitlines()
sequence
sequence= sequence[1:] #skips the sequence name (first line)
sequence= ''.join(sequence) #concatenates list to string

st.write('''
***
''')

## prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide Count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print Dictionary
st.subheader('1. Print Dictonary')
def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
    ("T",seq.count("T")),
    ("G",seq.count("G")),
    ("C",seq.count("C"))
    ])
    return d

X= DNA_nucleotide_count(sequence)

X_label= list(X)
X_values= list(X.values())

X


### 2. Print the text

st.subheader("2. Print Text")
st.write("There are "+ str(X["A"])+ " adenine (A)")
st.write("There are "+ str(X["A"])+ " thymine (T)")

st.write("There are "+ str(X["A"])+ " guanine (G)")

st.write("There are "+ str(X["A"])+ " cytosine (C)")

### 3. Display dataFrame 

st.subheader("3. Display dataFrame ")
df= pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0:'count'}, axis="columns")
df.reset_index(inplace=True)
df= df.rename(columns={'index':'nucleotide'})
st.write(df)

### 4. Display bar chart using using Altair

st.subheader("4. Display bar chart using using Altair")
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p= p.properties(
    width=alt.Step(80) # controls width of the bar
)
st.write(p)
