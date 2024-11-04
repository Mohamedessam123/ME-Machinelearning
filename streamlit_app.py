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
  st.
