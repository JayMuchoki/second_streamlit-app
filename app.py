import streamlit as st
 
st.title("hello world this is Maina")
st.title("Text Box Example")

# Add a text input box
user_input = st.text_input("Enter your name:")

# Display the entered text
if user_input:
    st.write(f"Hello, {user_input}!")

# Another example with a default value and a custom key
st.header("Feedback Form")
feedback = st.text_input("Provide your feedback:", "Type your thoughts here...", key="feedback_input")
st.write(f"Your feedback: {feedback}")

# A text area for multi-line input
st.header("Multi-line Text Input (Text Area)")
long_text = st.text_area("Enter a long message:", "Start typing your long message here...", height=150)
st.write(f"Your message: {long_text}")