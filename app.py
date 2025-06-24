import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Baca file CSV hasil klasifikasi Naive Bayes
    df = pd.read_csv("naivebayes_classification_results_fixed.csv")

    # Pemetaan label bahasa Inggris → Indonesia
    label_mapping = {
        'Positive': 'positif',
        'Negative': 'negatif',
        'Neutral': 'positif'  # jika ada netral, anggap positif
    }

    # Buat kolom label dalam bahasa Indonesia
    df['label'] = df['naivebayes_label'].map(label_mapping).fillna('positif')
    return df

# Load data
df = load_data()

# Judul aplikasi
st.title("🎬 Analisis Sentimen Film Jumbo")
st.write("Dataset ini memuat hasil klasifikasi sentimen dari ulasan film. Sentimen *netral* dianggap sebagai **positif**.")

# Pilih sentimen
sentiment = st.radio("Pilih Sentimen yang Ingin Ditampilkan:", ['positif', 'negatif'])

# Filter data
filtered_df = df[df['label'] == sentiment]

# Tampilkan data
st.subheader(f"📄 Data Sentimen: {sentiment.capitalize()}")
st.write(f"Jumlah data: {filtered_df.shape[0]}")
st.dataframe(filtered_df[['normalized_text', 'label']])

# Visualisasi
st.subheader("📊 Distribusi Sentimen")
st.bar_chart(df['label'].value_counts())
