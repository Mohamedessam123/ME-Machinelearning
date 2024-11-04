import streamlit as st
import pandas as pd
st.title('🤖 Machine-Learning App ..')
st.info('This is app Building a machine-Learning Model!')
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  st.write('**X**')
  x = df.drop('species', axis=1)
  x
  st.write('**Y**')
  y = df.species
  y
  st.table(df.iloc[0:10])
with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')
with st.sidebar:
  st.header("Input Features")
  island=st.selectbox("Island",('Biscoe','Dream','Torgersen'))
  gender=st.selectbox("gender",('Male','Female'))
  bill_length_mm = st.slider('Bill Length (MM) ',32.1,59.6,40.1)
  flipper_length_mm = st.slider('Flipper length (mm)',df.flipper_length_mm.min(),231.0,200.0)
  body_mass_g = st.slider('Body mass (g)',2700.0,6300.0,4200.0)

  
