import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
banner_pic = current_dir / "assets" / "cover-image.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Nikhil Idiculla"
PAGE_ICON = ":office_worker:"
NAME = "Nikhik Idiculla"
EMAIL = "nikhil.23.idiculla@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nikhil-idiculla/",
    "Github": "https://github.com/LiK-h1n"
}


# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- NAVIGATION ---
selected = option_menu(menu_title=None, options=["Home", "Education", "Projects", "Contact"],
                       icons=["house", "book", "braces", "envelope"], default_index=0, orientation="horizontal")


# --- LOAD CSS & PROFILE PIC ---
with open(css_file) as file:
    st.markdown("<style>{}</style>".format(file.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- CUSTOM FUNCTIONS FOR PRINTING TEXT
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


# --- HEADER ---
st.markdown("# Nikhil Idiculla", unsafe_allow_html=True)
st.image(profile_pic, width=200)
st.markdown("""
## About Me
- Hello! I'm Nikhil Idiculla, a passionate third-year BCA student. Python coding is my forte, and I'm on a dedicated 
path to becoming a data scientist.
- From scripting everyday solutions to building complex applications, Python's elegance has always intrigued me. 
- Welcome to my portfolio! Explore my data-driven projects and coding endeavors. Let's connect and explore the exciting 
world of technology and data together!
""", unsafe_allow_html=True)
