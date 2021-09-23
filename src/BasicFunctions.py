import streamlit as st
from PIL import Image
from pathlib import Path

@st.cache()
def load_image_file(file_name):
    return Image.open(file_name)

#@st.cache()
def read_video_file(file_name):
    return open(file_name, 'rb').read()

def read_markdown_file(file_name):
    return Path(file_name).read_text()

