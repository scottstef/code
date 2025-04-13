import pandas as pd
import os

def load_local_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        raise FileNotFoundError(f"No file found at {path}")

