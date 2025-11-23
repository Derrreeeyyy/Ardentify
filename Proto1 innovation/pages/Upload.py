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
    st.text_area ("Please enter: contact details, Secondary contact details, name, company/organization, where you found the artifact, hashtag/theme  and key notes", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible", width="stretch")





main()






