import streamlit as st
import requests

# Flask server URL
BASE_URL = "http://127.0.0.1:5000"

st.title("AI-Powered Chatbot and Image Tools")

# Navigation options
option = st.sidebar.selectbox(
    "Choose a Tool",
    ["Chatbot", "Image to Text", "Generate Image"]
)

# Chatbot Interface
if option == "Chatbot":
    st.header("Chat with AI")
    user_input = st.text_input("Enter your message:")
    if st.button("Send"):
        if user_input:
            response = requests.post(f"{BASE_URL}/chat", json={"message": user_input})
            if response.status_code == 200:
                st.success(response.json().get("response", "No response received"))
            else:
                st.error("Failed to get a response from the server.")

# Image to Text Interface
elif option == "Image to Text":
    st.header("Extract Text from Image")
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    if uploaded_file and st.button("Process Image"):
        files = {'image': uploaded_file}
        response = requests.post(f"{BASE_URL}/image-to-text", files=files)
        if response.status_code == 200:
            st.success(response.json().get("text", "No text detected"))
        else:
            st.error("Image processing failed.")

# Generate Image Interface
elif option == "Generate Image":
    st.header("Generate an AI Image")
    prompt = st.text_area("Enter a prompt for the image:")
    if st.button("Generate"):
        if prompt:
            response = requests.post(f"{BASE_URL}/generate-image", json={"prompt": prompt})
            if response.status_code == 200:
                image_url = response.json().get("image_url")
                if image_url:
                    st.image(image_url, caption="Generated Image")
            else:
                st.error("Failed to generate an image.")

# Footer
st.sidebar.info("This app uses a Flask backend for AI-powered functionalities.")

