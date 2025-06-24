import streamlit as st
import pandas as pd

# Fungsi untuk memberi label sentimen berdasarkan kata kunci
def get_sentiment(text):
    text = str(text).lower()
    positif_keywords = ['bagus', 'suka', 'keren', 'menarik', 'hebat', 'luar biasa']
    negatif_keywords = ['jelek', 'buruk', 'bosan', 'gagal', 'tidak suka', 'parah']

    if any(word in text for word in positif_keywords):
        return 'positif'
    elif any(word in text for word in negatif_keywords):
        return 'negatif'
    else:
        return 'netral'

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data_preprocessed.csv")
    if 'normalized_text' in df.columns:
        df['label'] = df['normalized_text'].apply(get_sentiment)
    elif 'full_text' in df.columns:
        df['label'] = df['full_text'].apply(get_sentiment)
    else:
        df['label'] = 'netral'
    return df

df = load_data()

# Judul
st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Analisis otomatis terhadap sentimen review film berdasarkan teks.")

# Pilihan sentimen
sentiment = st.radio("Pilih Sentimen:", ['positif', 'netral', 'negatif'])

filtered = df[df['label'] == sentiment]

st.subheader(f"Hasil Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered.shape[0]}")
st.dataframe(filtered[['normalized_text', 'label']])

# Statistik
st.subheader("Statistik Sentimen")
st.bar_chart(df['label'].value_counts())
