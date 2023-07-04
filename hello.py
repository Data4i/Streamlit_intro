import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({'firstcolumn': [1,2,4], 'secondcolumn': [5,7,9]})

print(df)

st.write(
    '''
    # HERE IS OUR FIRST APP
    '''
)
st.write(df)

dataframe = np.random.randn(10,20)

st.dataframe(dataframe)

dataframe2 = pd.DataFrame(
    np.random.randn(20,30),
    columns = ('col %d' % i for i in range(30))
)

st.dataframe(dataframe2.style.highlight_min(axis = 0))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)