import streamlit as st
import pandas as pd

# GUNAKAN RAW URL DARI GITHUB
CSV_URL = "https://raw.githubusercontent.com/bagusrizkiananda/jumbo/main/StemmingJumbo.csv"

st.set_page_config(page_title="Filter Sentimen", layout="wide")
st.title("Analisis Sentimen - Filter Tweet")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Data tidak dapat dimuat: {e}")
        return None

df = load_data()

if df is not None:
    # Periksa apakah kolom yang diperlukan ada
    required_cols = {'Tweet', 'Label'}
    if required_cols.issubset(df.columns):
        # Sidebar filter
        st.sidebar.header("Filter Sentimen")
        options = st.sidebar.multiselect(
            "Pilih label sentimen:",
            options=sorted(df['Label'].unique()),
            default=sorted(df['Label'].unique())
        )

        # Filter data
        filtered_df = df[df['Label'].isin(options)]

        st.write(f"Menampilkan {len(filtered_df)} data dengan label: {', '.join(options)}")
        st.dataframe(filtered_df[['Tweet', 'Label']], use_container_width=True)
    else:
        st.warning(f"Dataset harus memiliki kolom: {', '.join(required_cols)}")
