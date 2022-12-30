import streamlit as st
st.title("Hello")

col1,col2 = st.columns(2)

with col1:
    st.image('pic1.jpg')
with col2:
    st.write("""What is the meaning behind Hello?
Hello is first recorded in the early 1800s, but was originally used to attract attention or express surprise (“Well, hello! What do we have here?”). But the true breakthrough for this now-common word was when it was employed in the service of brand-new technology: the telephone""")

st.subheader('Hello World')
st.subheader('Hello India')
st.subheader('Hello USA')
st.subheader('Hello UK')