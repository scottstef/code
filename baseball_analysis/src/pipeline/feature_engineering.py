def add_features(df):
    df["slugging_plus_on_base"] = df["slg"] + df["obp"]
    df["is_power_hitter"] = df["hr"] > 20
    return df

