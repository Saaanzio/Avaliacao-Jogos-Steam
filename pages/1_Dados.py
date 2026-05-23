import streamlit as st
import pandas as pd
from games_service import get_processed_data


st.title("Dicionário e Tabela de Dados - Steam Games")
df = get_processed_data()
descricoes = {
    "AppID": "Identificador único do jogo",
    "Name": "Nome do jogo",
    "Price_USD": "Preço do jogo em dólares",
    "Review_Score_Pct": "Percentual de avaliações positivas",
    "Total_Reviews": "Quantidade total de avaliações",
    "Primary_Genre": "Gênero principal do jogo",
    "Release_Year": "Ano de lançamento"
}

dicionario = pd.DataFrame({
    "coluna": df.columns,
    "tipo": df.dtypes.astype(str),
    "exemplo": [df[col].dropna().iloc[0] if not df[col].dropna().empty else None for col in df.columns],
    "descricao": [descricoes[col] for col in df.columns]
})

st.header("Dicionário de Dados")
st.dataframe(dicionario, hide_index=True)

st.divider()

st.header("Tabela de Dados")
st.dataframe(df.head(5), hide_index=True, use_container_width=True)