import streamlit as st
from PIL import Image
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- LOAD CSS & PROFILE PIC ---
with open(css_file) as file:
    st.markdown("<style>{}</style>".format(file.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- HEADER ---
st.write("""
# Nikhil Idiculla
""")
