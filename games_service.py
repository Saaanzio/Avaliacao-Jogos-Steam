import pandas as pd


df = pd.read_csv("steam_games_2026.csv", sep=",", encoding="utf-8", index_col=False)

df = df[[
    "AppID",
    "Name",
    "Price_USD",
    "Discount_Pct",
    "Review_Score_Pct",
    "Total_Reviews",
    "Primary_Genre",
    "Release_Date",
    "Estimated_Owners",
    "24h_Peak_Players"
]]

def get_unprocessed_data():
    return df


def get_processed_data():
    df_processed = df.copy()

    df_processed = df_processed.dropna()

    df_processed["Release_Date"] = pd.to_datetime(
        df_processed["Release_Date"],
        errors="coerce"
    )

    df_processed["Release_Year"] = df_processed["Release_Date"].dt.year

    df_processed = df_processed.dropna(subset=["Release_Year"])

    df_processed["Release_Year"] = df_processed["Release_Year"].astype(int)

    df_processed = df_processed.drop(columns=["Release_Date"])

    df_processed = df_processed[
        (df_processed["Total_Reviews"] > 0) &
        (df_processed["Review_Score_Pct"] > 0)
    ]

    return df_processed