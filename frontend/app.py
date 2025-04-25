import streamlit as st
import requests
st.title("Image Captioning using LLaVA")
uploaded_file=st.file_uploader("Upload your image file",type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    if st.button("Generate Caption"):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("http://localhost:8000/image_caption/", files=files)
        caption = res.json().get("caption", "Error generating caption.")
        st.subheader("Caption:")
        st.write(caption)
