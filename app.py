import streamlit as st
import pandas as pd

# Load data lokal (ganti nama file sesuai kebutuhan)
df = pd.read_csv("StemmingJumbo.csv")

# Fungsi labeling sederhana berbasis keyword
def simple_sentiment(text):
    positive_keywords = ['bagus', 'menarik', 'keren', 'lucu', 'hebat', 'baik']
    negative_keywords = ['jelek', 'buruk', 'bosan', 'gagal', 'kurang', 'tidak']
    text = str(text).lower()
    if any(word in text for word in positive_keywords):
        return 'positif'
    elif any(word in text for word in negative_keywords):
        return 'negatif'
    else:
        return 'netral'

# Terapkan labeling ke kolom Tweet
df['label'] = df['Tweet'].apply(simple_sentiment)

# UI Streamlit
st.set_page_config(page_title="Filter Komentar", layout="centered")
st.title("🎭 Filter Komentar berdasarkan Sentimen")

# Pilihan label
sentimen = st.selectbox("Pilih jenis sentimen yang ingin ditampilkan:", ['positif', 'negatif', 'netral'])

# Filter data sesuai pilihan
filtered_df = df[df['label'] == sentimen]

# Tampilkan hasil
st.write(f"Menampilkan {len(filtered_df)} komentar dengan sentimen **{sentimen}**:")
st.dataframe(filtered_df[['Tweet']].reset_index(drop=True))
