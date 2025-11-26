import streamlit as st
from PIL import Image


def start():
    st.title("ARDENTIFY")
    st.subheader("Image upload")
    st.write("upload image of artifact")
def main():
 start()
 File = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

 if File is not None:
    image = Image.open(File)
    st.image(image, caption=None, width="content", use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=None)

 submit =  st.button("continue submission", key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")
 if submit:
  st.text_area("Name ,primary contact details, Secondary contact details, country and address of find and company/organisation", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible", width="stretch")


main()

























