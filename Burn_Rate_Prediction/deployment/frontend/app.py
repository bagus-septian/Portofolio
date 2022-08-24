import streamlit as st
import matplotlib.pyplot as plt
import requests

img = plt.imread("burnout.png")
st.image(img)

st.title("Aplikasi Pengecekan Tingkat Burning Out Pegawai")
gender = st.selectbox("Jenis kelamin", ["Male", "Female"])
wfh = st.selectbox("Apakah terdapat fasilitas WFH?",["Yes", "No"])
designation = st.number_input("Level Jabatan anda di perusahaan (skala 1-5, semakin tinggi skor semakin tinggi jabatan dalam perusahaan)")
resource = st.number_input("Berapa lama waktu yang anda alokasikan untuk bekerja dalam sehari (satuan jam)")
mental_score = st.number_input("Skor kelelahan mental anda (skala 1-10, semakin tinggi semakin parah kelelahan mental")

# inference
URL = "https://burn-rate-model-backend.herokuapp.com/burnout"
param = {'gender': gender,
         'wfh': wfh,
         'designation' : designation,
         'resource' :resource,
         'mental_score' : mental_score}
r = requests.post(URL, json=param)

st.write("Semakin tinggi burn rate anda semakin parah burnout yang dialami")