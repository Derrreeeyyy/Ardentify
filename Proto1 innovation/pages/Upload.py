import streamlit as st
from PIL import Image
import pickle


def start():
    st.title("ARDENTIFY")
    st.subheader("Image upload")
    st.write("upload image of artifact")
    st.write("""

    """)
def main():
 start()
 File = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

 if File is not None:
    image = Image.open(File)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.text_area ("What do you think the age of the artifact is
Where it is found at (longitude, latitude, place names) 
Characteristics (shapes, size)
How deep was it found
How many artifacts were near it
What artifacts were found near it
What type of artifact is it
What type of area/dig site was it found in (climate/biome) 
What the artifact is
Did you find it or did someone else find it?"), value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible", width="stretch")





main()








