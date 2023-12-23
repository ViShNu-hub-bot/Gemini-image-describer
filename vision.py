from dotenv import load_dotenv
load_dotenv()
#for loading environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function for loading our gemini
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input != "":
     response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image describer")

st.header("Gemini image Describer")
st.subheader("develope by vishnukanth.k")

input = st.text_input("input:",key="input")


uploaded_file = st.file_uploader("choose an image",type=["jpeg","jpg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)
    
submit = st.button("Describe the image to me")

if submit:

    response=get_gemini_response(input,image)
    st.subheader("the response is")
    st.write(response)