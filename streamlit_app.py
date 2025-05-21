import streamlit as st

st.title("🎈warpol no 1 pasti gacor")
st.write(
    "anjay ganteng banget gw"
)
st.image("IMG_20250415_074235.jpg") 
st.write("Maskot kami") 

st. title("SLOT TOGEL")
st. header("Pilih nomor")
angka = st.number_input("jackpot:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} ZONK")
else:
  st.write(f"{angka} Jackpot langsung WD")
