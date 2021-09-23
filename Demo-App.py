import streamlit as st
from BasicFunctions import read_markdown_file
from pathlib import Path
import sys

def begin():
    st.title('Welcome to 5G Portable Machines')
    company_description_file = str(Path.cwd())+'/Company_Description.md'
    markdown_company_description_text = read_markdown_file(company_description_file)
    st.markdown(markdown_company_description_text, unsafe_allow_html=False)

def machines():
    seed_sowing()


def contact_us():
    contact_us_file = str(Path.cwd())+'/Contact_Us.md'
    contact_us_checkbox = st.sidebar.checkbox('Contact Us', True)
    if contact_us_checkbox:
        markdown_contact_us_text = read_markdown_file(contact_us_file)
        st.markdown(markdown_contact_us_text, unsafe_allow_html=False)

if __name__ == '__main__':
    current_working_dir = str(Path.cwd())
    seed_sowing_path = current_working_dir+'/Seed_Sowing/'

    from SeedSowing import seed_sowing

    begin()
    machines()
    contact_us()
