import streamlit as st
from games_service import get_processed_data
from filters import apply_sidebar_filters
from styles import apply_custom_styles


st.set_page_config(page_title="Steam Games Analytics", page_icon="🎮", layout="wide")
apply_custom_styles()

df = get_processed_data()
df = apply_sidebar_filters(df)

st.title("🎮 Steam Games Analytics")
st.caption("Top 1000 jogos da Steam (2024-2026) — Fonte: Kaggle")

st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("🕹️ Total de Jogos", df.shape[0])
col2.metric("💲 Preco Medio", f"${df['Price_USD'].mean():.2f}")
col3.metric("⭐ Avaliacao Media", f"{df['Review_Score_Pct'].mean():.1f}%")
col4.metric("🆓 Jogos Gratis", f"{(df['Price_USD'] == 0).sum()}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📊 Jogos por Genero")
    genre_count = df["Primary_Genre"].value_counts()
    st.bar_chart(genre_count)

with right:
    st.subheader("🔥 Top 10 — Jogadores Ativos (24h)")
    top_players = df.nlargest(10, "24h_Peak_Players")[["Name", "24h_Peak_Players", "Primary_Genre"]]
    top_players = top_players.rename(columns={
        "Name": "Jogo",
        "24h_Peak_Players": "Pico 24h",
        "Primary_Genre": "Genero"
    })
    st.dataframe(top_players, hide_index=True, use_container_width=True)

st.divider()

left2, right2 = st.columns(2)

with left2:
    st.subheader("🏆 Top 10 — Mais Avaliados")
    top_reviewed = df.nlargest(10, "Total_Reviews")[["Name", "Total_Reviews", "Review_Score_Pct"]]
    top_reviewed = top_reviewed.rename(columns={
        "Name": "Jogo",
        "Total_Reviews": "Total Avaliacoes",
        "Review_Score_Pct": "% Positivas"
    })
    st.dataframe(top_reviewed, hide_index=True, use_container_width=True)

with right2:
    st.subheader("🏷️ Top 10 — Maiores Descontos")
    top_discount = df[df["Discount_Pct"] > 0].nlargest(10, "Discount_Pct")[["Name", "Discount_Pct", "Price_USD"]]
    top_discount = top_discount.rename(columns={
        "Name": "Jogo",
        "Discount_Pct": "Desconto %",
        "Price_USD": "Preco USD"
    })
    if top_discount.empty:
        st.info("Nenhum jogo com desconto ativo no momento.")
    else:
        st.dataframe(top_discount, hide_index=True, use_container_width=True)

st.divider()

st.markdown("""
<div class="project-info">
    <p><strong>📌 Sobre o Projeto</strong><br>
    Dashboard interativo para analise dos Top 1000 jogos da Steam.
    Os dados incluem precos, avaliacoes, generos, jogadores ativos e estimativa de donos.
    Navegue pelas paginas na sidebar para explorar os dados em detalhes.</p>
    <br>
    <p><strong>Grupo:</strong> Rafael Sanzio</p>
</div>
""", unsafe_allow_html=True)
