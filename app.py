import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("naivebayes_classification_results_fixed.csv")

    # Mapping label ke bahasa Indonesia.
    # 'Neutral' sekarang akan dipetakan ke 'netral' yang terpisah.
    label_mapping = {
        'Positive': 'positif',
        'Negative': 'negatif',
        'Neutral': 'netral'
    }

    # Menerapkan mapping dan menggunakan 'tidak diketahui' sebagai fallback
    # jika ada label yang tidak cocok dalam mapping.
    df['label'] = df['naivebayes_label'].map(label_mapping).fillna('tidak diketahui')
    return df

# Load data
df = load_data()

# Judul halaman
st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Analisis berdasarkan hasil klasifikasi Naive Bayes. Sentimen *netral* sekarang ditampilkan sebagai kategori terpisah.")

# Pilihan filter sentimen, sekarang mencakup 'netral'
sentiment = st.radio("Pilih Sentimen:", ['positif', 'negatif', 'netral'])

# Filter sesuai pilihan
filtered = df[df['label'] == sentiment]

# Tampilkan hasil
st.subheader(f"Hasil Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered.shape[0]}")
st.dataframe(filtered[['normalized_text', 'label']])

# Visualisasi
st.subheader("📊 Statistik Sentimen")
st.bar_chart(df['label'].value_counts())
