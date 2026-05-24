import streamlit as st
import pandas as pd
from games_service import get_processed_data
from filters import apply_sidebar_filters
from styles import apply_custom_styles


st.set_page_config(page_title="Dados - Steam Games", page_icon="📋", layout="wide")
apply_custom_styles()

df = get_processed_data()
df = apply_sidebar_filters(df)

st.title("📋 Dicionario e Tabela de Dados")

descricoes = {
    "AppID": "Identificador unico do jogo",
    "Name": "Nome do jogo",
    "Price_USD": "Preco do jogo em dolares",
    "Discount_Pct": "Percentual de desconto atual",
    "Review_Score_Pct": "Percentual de avaliacoes positivas",
    "Total_Reviews": "Quantidade total de avaliacoes",
    "Primary_Genre": "Genero principal do jogo",
    "Release_Year": "Ano de lancamento",
    "Estimated_Owners": "Estimativa de donos do jogo",
    "24h_Peak_Players": "Pico de jogadores nas ultimas 24h"
}

dicionario = pd.DataFrame({
    "Coluna": df.columns,
    "Tipo": df.dtypes.astype(str),
    "Exemplo": [df[col].dropna().iloc[0] if not df[col].dropna().empty else None for col in df.columns],
    "Descricao": [descricoes.get(col, "-") for col in df.columns]
})

st.subheader("📖 Dicionario de Dados")
st.dataframe(dicionario, hide_index=True, use_container_width=True)

st.divider()

st.subheader("📊 Tabela de Dados")
rows = st.slider("Linhas exibidas", min_value=5, max_value=min(50, df.shape[0]), value=10, step=5)
st.dataframe(df.head(rows), hide_index=True, use_container_width=True)
