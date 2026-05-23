import streamlit as st
from games_service import get_processed_data


df =  get_processed_data()

st.title("Análise Estatística - Steam Games")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Preço médio",
    f"${df['Price_USD'].mean():.2f}"
)

col2.metric(
    "Mediana do preço",
    f"${df['Price_USD'].median():.2f}"
)

col3.metric(
    "Desvio padrão do preço",
    f"${df['Price_USD'].std():.2f}"
)

st.divider()

col4, col5, col6 = st.columns(3)

col4.metric(
    "Avaliação média",
    f"{df['Review_Score_Pct'].mean():.1f}%"
)

col5.metric(
    "Mediana da avaliação",
    f"{df['Review_Score_Pct'].median():.1f}%"
)

col6.metric(
    "Desvio padrão avaliação",
    f"{df['Review_Score_Pct'].std():.2f}"
)

st.divider()

col7, col8, col9 = st.columns(3)

col7.metric(
    "Total de jogos",
    df.shape[0]
)

col8.metric(
    "Gênero mais comum",
    df["Primary_Genre"].mode()[0]
)

col9.metric(
    "Ano com mais lançamentos",
    df["Release_Year"].value_counts().idxmax()
)

st.divider()

col10, col11, col12 = st.columns(3)

col10.metric(
    "Jogos grátis (%)",
    f"{(df['Price_USD'] == 0).mean() * 100:.1f}%"
)

col11.metric(
    "Correlação preço x avaliação",
    f"{df[['Price_USD','Review_Score_Pct']].corr().iloc[0,1]:.2f}"
)

col12.metric(
    "Total de avaliações (média)",
    f"{df['Total_Reviews'].mean():.0f}"
)