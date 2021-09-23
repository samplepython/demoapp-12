import streamlit as st
from pathlib import Path
import sys

main_working_dir = str(Path.cwd())
basic_src_path = main_working_dir+'/src'
sys.path.insert(0, basic_src_path)
from BasicFunctions import load_image_file, read_video_file, read_markdown_file

def seed_sowing():
    seed_sowing_machine_checkbox = st.sidebar.checkbox('Seed Sowing Machine', False)
    if seed_sowing_machine_checkbox:
        st.header('Seed Sowing Machine')
        # Description
        seed_sowing_description_file = main_working_dir+'/seed_sowing/static/Seed_Sowing_Description.md'
        markdown_seed_sowing_description_text = read_markdown_file(seed_sowing_description_file)
        st.markdown(markdown_seed_sowing_description_text, unsafe_allow_html=False)


        # Images
        st.caption('Basic Model')
        image_file = main_working_dir + '/seed_sowing/media/Machine.jpg'
        loaded_image = load_image_file(image_file)
        st.image(loaded_image)

    	# Videos
        st.header('Onion Seeds Sowing Demo')
        onion_video_file = main_working_dir+'/seed_sowing/media/OnionSowing.mp4'
        video_bytes = read_video_file(onion_video_file)
        st.video(video_bytes)
