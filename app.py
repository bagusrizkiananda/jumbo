import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("naivebayes_classification_results.csv")
    
    # Pastikan kolom label tersedia
    if 'naivebayes_label' in df.columns:
        # Ubah semua label netral menjadi positif
        df['label'] = df['naivebayes_label'].replace('netral', 'positif')
    else:
        df['label'] = 'positif'  # fallback
    return df

df = load_data()

# Judul Aplikasi
st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Analisis menggunakan hasil klasifikasi Naive Bayes. Semua sentimen netral dianggap positif.")

# Pilihan Sentimen
sentiment = st.radio("Pilih Sentimen:", ['positif', 'negatif'])

# Filter data
filtered = df[df['label'] == sentiment]

st.subheader(f"Hasil Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered.shape[0]}")
st.dataframe(filtered[['normalized_text', 'label']])

# Statistik
st.subheader("Statistik Sentimen")
st.bar_chart(df['label'].value_counts())
