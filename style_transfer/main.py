import streamlit as st
from PIL import Image
import style
import os
import gc
from utils import local_css, remote_css

gc.enable()
st.set_page_config(layout="wide")
st.title("Neural Style Transfer")
st.write(
    "#### Written by [Zito Relova](https://github.com/zitorelova/neural-style-app)"
)

path = os.path.dirname(__file__)
local_css(os.path.join(path, "css/style.css"))
remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")

content_list = [
    img.split(".jpg")[0]
    for img in os.listdir(os.path.join(path, "images/content-images"))
]
style_list = [
    img.split(".jpg")[0]
    for img in os.listdir(os.path.join(path, "images/style-images"))
]
content_list.append("Select your own")
content_img = st.sidebar.selectbox("Select Content Image", content_list)
style_img = st.sidebar.selectbox("Select Style Image", style_list)

content_col, style_col = st.beta_columns(2)

if content_img == "Select your own":
    image_file = content_col.file_uploader(
        "Upload your own content image for style transfer",
        type=["png", "jpg", "jpeg"])

    if image_file:
        loaded_content_image = image_file.read()
        content_path = loaded_content_image
        content_col.image(loaded_content_image, width=400, caption="Content Image")
else:
    content_path = os.path.join(path, f"images/content-images/{content_img}.jpg")
    loaded_content_image = Image.open(content_path).resize((400, 400))
    content_col.image(loaded_content_image, width=400, caption="Content Image")

model = os.path.join(path, f"saved_models/{style_img}.pth")
style_path = os.path.join(path, f"images/style-images/{style_img}.jpg")
output_image = os.path.join(
    path, f"./images/output-images/{style_img}-{content_img}.jpg"
)

loaded_style_image = Image.open(style_path)
style_col.image(loaded_style_image, width=400, caption="Style Image")

st.text("")
_, use_col, _ = st.beta_columns(3)
_, img_col, _ = st.beta_columns([1.85, 3, 2.5])

clicked = use_col.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, content_path, output_image)
    image = Image.open(output_image)
    img_col.image(image, width=400, caption="Output Image")
