import streamlit as st

st.title("AI Construction Assistant")

question = st.text_input("Ask a construction question")

if question:
    if "steel weight" in question.lower():
        st.write("Steel Weight = D²/162 kg/m")
    elif "cube test" in question.lower():
        st.write("Cube test is conducted at 7 and 28 days.")
    else:
        st.write("Construction query received.")
