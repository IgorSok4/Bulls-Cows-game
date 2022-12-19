import streamlit as st
import pandas as pd
import classes

options = classes.GameOptions()

st.subheader("In this section you can change game options")
st.info(f"Currently set: {options.getOptions()[0]} letters, {options.getOptions()[1]} attempts", icon="ℹ️")


df = pd.DataFrame({
    'first column': [4, 5, 6],
    'second column': [5, 8, 12]
    })

option_word_lenght = st.selectbox(
    'Change number of letters in the word.',
     df['first column'])

'You selected: ', option_word_lenght

option_attmepts = st.selectbox(
    'Cghange number of attempts in the new game.',
    df['second column']
)
'You selected: ', option_attmepts