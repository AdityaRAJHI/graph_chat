import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Streamlit Graph App')

# Generate some random data
np.random.seed(0)
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100).cumsum()
})

# Create a line chart
chart = alt.Chart(data).mark_line().encode(
    x='x',
    y='y'
).properties(
    title='Simple Line Chart'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

st.write("This is a simple Streamlit app that displays a line chart.")

# Chatbot functionality
st.subheader("Chatbot")

st.write("Chatbot functionality is not available in this environment.")
