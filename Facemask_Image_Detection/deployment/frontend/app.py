import json
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import requests

# Set header image
header = plt.imread("data/facemask_reg.png")
st.image(header)

# Set title
st.title("Aplikasi Pengecekan Face Mask")

# Input image
upload = st.file_uploader('Masukkan gambar untuk pengecekan', type=['png','jpg', 'jpeg'])

if upload is not None:
    image = Image.open(upload)
    st.image(image)


    img = Image.open(upload)
    # Define image size
    size = (150,150)
    # Convert input image to size
    resize = ImageOps.fit(image, size, Image.ANTIALIAS)
    # Convert image to array
    imgs_array = np.asarray(resize)
    # Expand array
    new_data = np.expand_dims(imgs_array, 0)

    # Convert array to list
    new_data = new_data.tolist()
    

    # inference
    URL = 'http://face-mask-ml2p2-backend.herokuapp.com/v1/models/facemask_model:predict'
    param = json.dumps({
            "signature_name":"serving_default",
            "instances":new_data
        })
    r = requests.post(URL, data=param)

    if r.status_code == 200:
        res = r.json()
        if res['predictions'][0][0] > 0.5:
            st.title("Maaf, Anda tidak menggunakan masker")
        else:
            st.title("Terima kasih, Anda sudah menggunakan masker")
    else:
        st.title("Unexpected Error")
else:
    st.title("Silakan upload gambar terlebih dahulu")