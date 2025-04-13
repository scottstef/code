def clean_baseball_data(df):
    # Drop missing values, normalize column names, convert types
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df.dropna(subset=["player", "team"], inplace=True)
    return df

