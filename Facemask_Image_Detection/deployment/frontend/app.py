import json
import matplotlib.pyplt as plt
import cv2
import numpy as np
import streamlit as st
import requests

# Set header image
header = cv2.imread("model/facemask.jpg")
st.image(cv2.cvtColor(header, cv2.COLOR_BGR2RGB))

# Set title
st.title("Aplikasi Pengecekan Face Mask")

# Input image
upload = st.file_uploader('Masukkan gambar untuk pengecekan', type=['png','jpg'])

# Open input image
inf = plt.imread(upload)
# Convert image to array
imgs = np.asarray(inf)
# Convert input image to size
img = cv2.resize(imgs, (150,150))
# Expand array
new_data = np.expand_dims(imgs, 0)

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