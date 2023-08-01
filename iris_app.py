import streamlit as st
import numpy as np
import joblib

st.markdown ('## Iris Species Prediction' )
sepal_length = st.number_input ('sepal length (cm) ')
sepal_width = st.number_input (' sepal width (cm)')
petal_length =st.number_input( 'petal length (cm)')
petal_width = st.number_input ('petal width (cm)')

#Predict button
if st.button(' Predict'):
  model = joblib.load( 'iris_model.pkl')
  X = np. array ([sepal_length, sepal_width, petal_length, petal_width])
  if any(X <= 0):
    st.markdownt('## Inputs must be greater than 0')
  else:
      st.markdown (f'### Prediction is {model.predict([[sepal_length, sepal_width,petal_length, petal_width]])[0]}')
