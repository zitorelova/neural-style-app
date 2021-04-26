import streamlit as st
from PIL import Image
import style
import os
from utils import local_css, remote_css

st.set_page_config(layout="wide")
st.title("Style Transfer")
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

content_img = st.sidebar.selectbox("Select Content Image", content_list)
style_img = st.sidebar.selectbox("Select Style Image", style_list)

model = os.path.join(path, f"saved_models/{style_img}.pth")
content_path = os.path.join(path, f"images/content-images/{content_img}.jpg")
style_path = os.path.join(path, f"images/style-images/{style_img}.jpg")
output_image = os.path.join(
    path, f"./images/output-images/{style_img}-{content_img}.jpg"
)

content_col, style_col = st.beta_columns(2)


content_col.write("### Content Image")
style_col.write("### Style Image")
loaded_content_image = Image.open(content_path)
loaded_style_image = Image.open(style_path)
content_col.image(
    loaded_content_image,
    width=400,
)
style_col.image(loaded_style_image, width=400)

_, use_col, _ = st.beta_columns(3)
clicked = use_col.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, content_path, output_image)

    use_col.write("### Output Image")
    image = Image.open(output_image)
    use_col.image(image, width=400)
