import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("naivebayes_classification_results.csv")

    # Mapping label ke bahasa Indonesia dan konsisten
    label_mapping = {
        'Positive': 'positif',
        'Negative': 'negatif',
        'Neutral': 'positif'  # jika ada label 'Neutral' di masa depan
    }

    df['label'] = df['naivebayes_label'].map(label_mapping).fillna('positif')
    return df

# Load data
df = load_data()

# Judul halaman
st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Analisis berdasarkan hasil klasifikasi Naive Bayes. Semua sentimen *netral* dianggap **positif**.")

# Pilihan filter
sentiment = st.radio("Pilih Sentimen:", ['positif', 'negatif'])

# Filter sesuai pilihan
filtered = df[df['label'] == sentiment]

# Tampilkan hasil
st.subheader(f"Hasil Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered.shape[0]}")
st.dataframe(filtered[['normalized_text', 'label']])

# Visualisasi
st.subheader("📊 Statistik Sentimen")
st.bar_chart(df['label'].value_counts())
