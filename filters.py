import streamlit as st
import pandas as pd


def apply_sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filtros")

    genres = sorted(df["Primary_Genre"].unique())
    selected_genres = st.sidebar.multiselect("Genero", genres, default=genres)

    price_min = float(df["Price_USD"].min())
    price_max = float(df["Price_USD"].max())
    price_range = st.sidebar.slider(
        "Faixa de Preco (USD)",
        min_value=price_min,
        max_value=price_max,
        value=(price_min, price_max),
        step=1.0
    )

    years = sorted(df["Release_Year"].unique())
    year_range = st.sidebar.slider(
        "Ano de Lancamento",
        min_value=int(min(years)),
        max_value=int(max(years)),
        value=(int(min(years)), int(max(years)))
    )

    filtered = df[
        (df["Primary_Genre"].isin(selected_genres)) &
        (df["Price_USD"] >= price_range[0]) &
        (df["Price_USD"] <= price_range[1]) &
        (df["Release_Year"] >= year_range[0]) &
        (df["Release_Year"] <= year_range[1])
    ]

    st.sidebar.caption(f"{filtered.shape[0]} de {df.shape[0]} jogos")

    return filtered
