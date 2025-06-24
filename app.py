import streamlit as st
import pandas as pd

st.set_page_config(page_title="Filter Komentar", layout="centered")
st.title("🎭 Filter Komentar berdasarkan Sentimen")

# Load data
df = pd.read_csv("StemmingJumbo.csv")

# DEBUG: tampilkan semua kolom
st.write("Kolom yang tersedia di CSV:")
st.write(df.columns.tolist())

# Gunakan kolom yang benar untuk analisis sentimen
# Misalnya kamu ingin pakai kolom 'Stemming'
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

df['label'] = df['Stemming'].apply(simple_sentiment)

sentimen = st.selectbox("Pilih jenis sentimen yang ingin ditampilkan:", ['positif', 'negatif', 'netral'])

filtered_df = df[df['label'] == sentimen]

st.write(f"Menampilkan {len(filtered_df)} komentar dengan sentimen **{sentimen}**:")
st.dataframe(filtered_df[['Stemming']].reset_index(drop=True))
