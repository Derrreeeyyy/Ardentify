import streamlit as st
import pickle


def start():
    st.title("ARDENTIFY")
    st.image("c:/Users/ricew/OneDrive/Documents/legend-of-bob/Assets/logo.png", caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=None)
    st.subheader("Live Photo")
    st.write("Take a live photo of artifact")
    st.write("""

    """)
    if st.button("start camera"):
        st.write("Camera started")
        photo = st.camera_input("Take a photo")
        if st.button("Detect Objects"):
           st.write("cool")


def main():
 start()




main()
