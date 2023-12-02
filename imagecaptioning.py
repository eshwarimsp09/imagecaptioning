from PIL import Image
import requests
import streamlit as st
import io

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

st.title("Image Captioning")

def query(filename):
    data = filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
prompt = st.text_input("Enter your prompt")
button_prompt = st.button("Generate Image")
if button_prompt:
    st.image(prompt,caption="Image uploaded")
    output = query(prompt)
    st.write(output[0]["generated_text"])
