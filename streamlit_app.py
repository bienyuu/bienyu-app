import streamlit as st

st.title("🎈warpol-no-1-pasti-gacor")
st.write(
    "anjay-ganteng-banget-gw"
)
st.image("IMG_20250415_074235.jpg") 

st. title("aplikasi sederhana")
st. header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
