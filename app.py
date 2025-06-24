import streamlit as st
import pandas as pd

# URL GitHub (ganti nanti dengan URL file CSV kamu di GitHub)
CSV_URL = "https://raw.githubusercontent.com/username/repo/main/StemmingJumbo.csv"

st.set_page_config(page_title="Filter Sentimen", layout="wide")

st.title("Analisis Sentimen - Filter Tweet")

# Load dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Data tidak dapat dimuat: {e}")
        return pd.DataFrame()

df = load_data()

# Pastikan kolom 'Label' dan 'Tweet' ada
if not all(col in df.columns for col in ['Tweet', 'Label']):
    st.warning("Dataset tidak memiliki kolom 'Tweet' atau 'Label'.")
else:
    # Opsi filter sentimen
    st.sidebar.header("Filter Sentimen")
    options = st.sidebar.multiselect(
        "Pilih label sentimen:",
        options=df['Label'].unique(),
        default=df['Label'].unique()
    )

    # Filter data
    filtered_df = df[df['Label'].isin(options)]

    st.write(f"Menampilkan {len(filtered_df)} data dengan label: {', '.join(options)}")
    st.dataframe(filtered_df[['Tweet', 'Label']], use_container_width=True)
