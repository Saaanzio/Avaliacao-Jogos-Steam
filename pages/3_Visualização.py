import streamlit as st
from games_service import get_processed_data


df = get_processed_data()

st.header("Analise Estatística e Visualização")

genre_avg = df.groupby("Primary_Genre")["Review_Score_Pct"].mean().sort_values(ascending=False)

st.subheader("Média de avaliações positivas por gênero")
st.bar_chart(genre_avg)

st.subheader("Relação entre preço e avaliações positivas")

st.scatter_chart(df[["Price_USD", "Review_Score_Pct"]])

year_counts = df["Release_Year"].value_counts().sort_index()

st.subheader("Número de lançamentos por ano")
st.bar_chart(year_counts)

st.subheader("Comparação: jogos grátis vs pagos")

df["Is_Free"] = df["Price_USD"] == 0

free_vs_paid = df.groupby("Is_Free")["Review_Score_Pct"].mean()

st.bar_chart(free_vs_paid)

st.subheader("Top 10 jogos mais bem avaliados")
top_rated = df.sort_values("Review_Score_Pct", ascending=False).head(10)
st.dataframe(top_rated[["Name", "Review_Score_Pct", "Primary_Genre", "Price_USD"]], use_container_width=True)

st.subheader("Quantidade de jogos por gênero")

genre_count = df["Primary_Genre"].value_counts()

st.bar_chart(genre_count)