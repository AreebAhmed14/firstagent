from main import suggestionai
import streamlit as st

st.set_page_config(page_title="areebix.suggest" , page_icon="sugges.png")
st.title("AREEBIX SUGGEST🔮")

user = st.chat_input("Ask question...")

if user:
  st.info(f"{user}")

if user:
    result = suggestionai(user)
    st.write(result)
