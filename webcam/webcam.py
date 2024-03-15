import streamlit as st
from PIL import Image

with st.expander("start camera"):
    # start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # we convert the image to gray scale
    gray_img = img.convert("L")
    st.image(gray_img)
