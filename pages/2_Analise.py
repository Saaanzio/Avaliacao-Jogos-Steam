import streamlit as st
from games_service import get_processed_data
from filters import apply_sidebar_filters
from styles import apply_custom_styles


st.set_page_config(page_title="Analise - Steam Games", page_icon="📈", layout="wide")
apply_custom_styles()

df = get_processed_data()
df = apply_sidebar_filters(df)

st.title("📈 Analise Estatistica")

st.subheader("💲 Precos")
col1, col2, col3 = st.columns(3)
col1.metric("Preco medio", f"${df['Price_USD'].mean():.2f}")
col2.metric("Mediana", f"${df['Price_USD'].median():.2f}")
col3.metric("Desvio padrao", f"${df['Price_USD'].std():.2f}")

st.divider()

st.subheader("⭐ Avaliacoes")
col4, col5, col6 = st.columns(3)
col4.metric("Avaliacao media", f"{df['Review_Score_Pct'].mean():.1f}%")
col5.metric("Mediana", f"{df['Review_Score_Pct'].median():.1f}%")
col6.metric("Desvio padrao", f"{df['Review_Score_Pct'].std():.2f}")

st.divider()

st.subheader("🎯 Geral")
col7, col8 = st.columns(2)
col7.metric("Total de jogos", df.shape[0])
col8.metric("Genero mais comum", df["Primary_Genre"].mode()[0] if not df.empty else "-")

col9, col10 = st.columns(2)
col9.metric("Jogos gratis", f"{(df['Price_USD'] == 0).sum()}")
col10.metric("Correlacao preco x avaliacao", f"{df[['Price_USD','Review_Score_Pct']].corr().iloc[0,1]:.2f}" if len(df) > 1 else "-")

st.divider()

st.subheader("👥 Jogadores e Popularidade")
col11, col12 = st.columns(2)
col11.metric("Media de donos estimados", f"{df['Estimated_Owners'].mean():,.0f}")
col12.metric("Media jogadores ativos (24h)", f"{df['24h_Peak_Players'].mean():,.0f}")
