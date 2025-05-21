import streamlit as st

st.title("🎈warpol no 1 pasti gacor")
st.write(
    "anjay ganteng banget gw"
)
st.image("IMG_20250415_074235.jpg") 

st. title("togel")
st. header("Nomor togel")
angka = st.number_input("jackpot:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} zonk")
else:
  st.write(f"{angka} jackpot")
