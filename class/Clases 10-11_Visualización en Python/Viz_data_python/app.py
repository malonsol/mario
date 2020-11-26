
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.button('say hello')

agree = st.checkbox('yes')
genre = st.radio("What's your favorite color?", ('red','black','yellow'))

st.write(genre)

st.selectbox('color?', ('red','blue'))
