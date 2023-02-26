import streamlit as st



st.title("I am :blue[Nilesh Shinde]:sunglasses:")
st.snow()
st.header("My info.")

st.subheader("My name")
code = '''print("Hello World")'''

st.code(code, language="python")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()