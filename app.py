import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data_preprocessed.csv")

df = load_data()

# Judul
st.title("📽️ Analisis Sentimen Film Jumbo")
st.write("Aplikasi ini memfilter review berdasarkan hasil sentimen: positif, netral, atau negatif.")

# Pratinjau data
st.subheader("Pratinjau Dataset")
st.dataframe(df.head())

# Cek apakah kolom label tersedia
if 'label' not in df.columns:
    st.error("Kolom 'label' tidak ditemukan dalam dataset. Pastikan file CSV memiliki kolom ini.")
else:
    # Filter berdasarkan label
    option = st.radio("Pilih kategori sentimen:", ['positif', 'netral', 'negatif'])

    filtered_df = df[df['label'].str.lower() == option.lower()]

    st.subheader(f"Hasil Sentimen: {option.capitalize()}")
    st.write(f"Jumlah data: {filtered_df.shape[0]}")
    st.dataframe(filtered_df)

    # Statistik total sentimen
    st.subheader("Statistik Keseluruhan Sentimen")
    st.bar_chart(df['label'].value_counts())
