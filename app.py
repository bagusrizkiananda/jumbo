import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("naivebayes_classification_results.csv")
    if 'naivebayes_label' in df.columns:
        # Pastikan bersih dan lowercase
        df['label'] = df['naivebayes_label'].str.strip().str.lower().replace('netral', 'positif')
    else:
        df['label'] = 'positif'
    return df

df = load_data()

st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Analisis menggunakan hasil klasifikasi Naive Bayes. Semua sentimen netral dianggap positif.")

sentiment = st.radio("Pilih Sentimen:", ['positif', 'negatif'])

filtered = df[df['label'] == sentiment]

st.subheader(f"Hasil Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered.shape[0]}")
st.dataframe(filtered[['normalized_text', 'label']])

st.subheader("Statistik Sentimen")
st.bar_chart(df['label'].value_counts())
