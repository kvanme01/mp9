import requests
import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_coding = load_lottieurl("https://lottie.host/fa929178-b313-4117-81a7-5d65930814b0/dwnoELXyMg.json")

# Load GPT-2 for text generation
gpt2_model = pipeline("text-generation", model="gpt2")

# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon="ta:da", layout="wide")

# Header section
with st.container():
    st.subheader("Hi :wave:")
    st.title("Welcome to my professional website")
    st.write("To visit my GitHub repo [click here](https://github.com/kvanme01)")

# Subheader section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I am a data scientist with a passion for building web applications and data analysis.")
        st.write("I have experience in Python, SQL, and Tableau. I am currently working on a project to automate the data analysis process.")
        st.write("In my free time, I enjoy woodworking, astrophotography, and baking artisan bread.")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# GPT-2 section
with st.container():
    st.write("---")
    st.header("Converse with GPT-2")
    st.write("##")
    st.write("I like to experiment with LLMs. I have added in a GPT-2 model that can generate text based on your input. Try it out here.")

    # User input
    user_input = st.text_input("Enter your prompt:")

    # Generate button
    if st.button("Generate"):
        try:
            # Generate text based on user input
            generated_text = gpt2_model(user_input, max_length=100, truncation=True)[0]['generated_text']
            # Display generated text
            st.write("Generated Response:")
            st.write(generated_text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")






