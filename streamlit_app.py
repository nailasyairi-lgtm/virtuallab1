import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualisasi Cara Kita Menimbang")

st.write("Masukkan data berat hasil penimbangan")

# Input data
hari = st.text_input("Hari")
berat = st.number_input("Berat (kg)", min_value=0.0)

# Simpan data sementara
if "data" not in st.session_state:
    st.session_state.data = []

if st.button("Tambah Data"):
    st.session_state.data.append({
 "Hari": hari,
        "Berat": berat
    })
# Tampilkan tabel
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)

    st.subheader("Data Penimbangan")
    st.dataframe(df)

    # Grafik
    fig, ax = plt.subplots()
    ax.plot(df["Hari"], df["Berat"], marker='o')
    ax.set_xlabel("Hari")
    ax.set_ylabel("Berat (kg)")
    ax.set_title("Grafik Penimbangan")

    st.pyplot(fig)
