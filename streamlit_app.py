import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello Streamlit')

st.write("This is a simple Streamlit app deployed from GitHub!")

# Example DataFrame
df = pd.DataFrame({
    'Column 1': np.random.randn(100),
    'Column 2': np.random.randn(100)
})

st.line_chart(df)
