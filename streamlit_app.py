# streamlit_app.py
import streamlit as st
import subprocess
import base64

try:
    from PIL import Image
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "Pillow"])
    from PIL import Image  # Import again after installation

def get_image_download_link(img_path, filename):
    with open(img_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
        return f'<a href="data:image/png;base64,{b64}" download="{filename}">Download {filename}</a>'


st.title("Image Encryption & Decryption")

option = st.radio("Choose an action:", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    # Accept user input for the message
    message = st.text_input("Enter your message to encrypt:")

    if st.button("Encrypt"):
        # Save the message to 'msg.txt'
        with open("msg.txt", "w") as file:
            file.write(message)

        # Run the required scripts
        scripts = ["asciiToImg.py", "privateKeyGenerator.py", "publicKeyGenerator.py", "encrypt.py"]
        for script in scripts:
            subprocess.run(["python", script])

        # Display the resulting images with download links
        st.image("pk.png", caption="Private Key Image")
        st.markdown(get_image_download_link("pk.png", "pk.png"), unsafe_allow_html=True)

        st.image("pub.png", caption="Public Key Image")
        st.markdown(get_image_download_link("pub.png", "pub.png"), unsafe_allow_html=True)

        st.image("enc.png", caption="Encrypted Image")
        st.markdown(get_image_download_link("enc.png", "enc.png"), unsafe_allow_html=True)

elif option == "Decrypt":
    # Allow user to upload the necessary images
    uploaded_pk = st.file_uploader("Upload Private Key Image (pk.png)", type=["png"])
    uploaded_pub = st.file_uploader("Upload Public Key Image (pub.png)", type=["png"])
    uploaded_enc = st.file_uploader("Upload Encrypted Image (enc.png)", type=["png"])

    if st.button("Decrypt") and uploaded_pk and uploaded_pub and uploaded_enc:
        # Save the uploaded images
        with open("pk.png", "wb") as file:
            file.write(uploaded_pk.getvalue())
        with open("pub.png", "wb") as file:
            file.write(uploaded_pub.getvalue())
        with open("enc.png", "wb") as file:
            file.write(uploaded_enc.getvalue())

        # Run the decryption script
        subprocess.run(["python", "decrypt.py"])

        # Display the decrypted message
        with open("decryptedMessage.txt", "r") as file:
            decrypted_message = file.read()
        st.text_area("Decrypted Message:", decrypted_message)

st.write("Note: Click the button after making your selection and/or entering your message.")