import streamlit as st
from games_service import get_processed_data
from filters import apply_sidebar_filters
from styles import apply_custom_styles


st.set_page_config(page_title="Visualizacao - Steam Games", page_icon="📊", layout="wide")
apply_custom_styles()

df = get_processed_data()
df = apply_sidebar_filters(df)

st.title("📊 Visualizacao de Dados")

st.subheader("⭐ Media de avaliacoes positivas por genero")
genre_avg = df.groupby("Primary_Genre")["Review_Score_Pct"].mean().sort_values(ascending=False)
st.bar_chart(genre_avg)

st.divider()

st.subheader("💲 Relacao entre preco e avaliacoes")
st.scatter_chart(df, x="Price_USD", y="Review_Score_Pct", color="Primary_Genre")

st.divider()

st.subheader("📅 Lancamentos por ano")
year_counts = df["Release_Year"].value_counts().sort_index()
st.bar_chart(year_counts)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🆓 Gratis vs Pagos")
    df_copy = df.copy()
    df_copy["Tipo"] = df_copy["Price_USD"].apply(lambda x: "Gratis" if x == 0 else "Pago")
    free_vs_paid = df_copy.groupby("Tipo")["Review_Score_Pct"].mean()
    st.bar_chart(free_vs_paid)

with right:
    st.subheader("🏆 Top 10 — Melhor Avaliados")
    top_rated = df.sort_values("Review_Score_Pct", ascending=False).head(10)
    st.dataframe(
        top_rated[["Name", "Review_Score_Pct", "Primary_Genre", "Price_USD"]],
        use_container_width=True,
        hide_index=True
    )

st.divider()

left2, right2 = st.columns(2)

with left2:
    st.subheader("🎮 Jogos por Genero")
    genre_count = df["Primary_Genre"].value_counts()
    st.bar_chart(genre_count)

with right2:
    st.subheader("👥 Top 10 — Donos Estimados")
    top_owners = df.nlargest(10, "Estimated_Owners")[["Name", "Estimated_Owners", "Primary_Genre"]]
    top_owners = top_owners.rename(columns={
        "Name": "Jogo",
        "Estimated_Owners": "Donos Estimados",
        "Primary_Genre": "Genero"
    })
    st.dataframe(top_owners, hide_index=True, use_container_width=True)
