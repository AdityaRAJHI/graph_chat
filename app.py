import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from huggingface_hub import InferenceClient

st.title('Streamlit Graph App')

# Sidebar for API key input
api_key = st.sidebar.text_input("Hugging Face API Key", type="password")

client = InferenceClient(
	api_key=api_key
)

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

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Say something"):
    # Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {"role": "user", "content": prompt}
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct", 
        messages=messages, 
        max_tokens=500,
    )

    response = completion.choices[0].message["content"]

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
