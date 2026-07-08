import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from chat import ask_ai

st.set_page_config(
    page_title="EngineerGPT",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 EngineerGPT")
st.write("Your Personal AI Engineering Assistant")

question = st.text_area(
    "Ask anything...",
    height=150
)

if st.button("Generate Response"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            answer = ask_ai(question)

        st.success("Done!")

        st.markdown("### Response")

        st.write(answer)