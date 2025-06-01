from main import shajition
import streamlit as st

st.set_page_config(page_title="shajition" , page_icon="shajition.png")
st.title("SHAJITION🔮")

user = st.chat_input("Ask question...")


if user:
    result = shajition(user)
    st.info(user)
    st.write(result)