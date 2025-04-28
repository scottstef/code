ifrom src.config import RAW_DATA_PATH, CLEAN_DATA_PATH
from src.pipeline import fetch_data, clean_data, feature_engineering
from src import visualize, model

def main():
    df = fetch_data.load_local_data(RAW_DATA_PATH)
    df = clean_data.clean_baseball_data(df)
    df = feature_engineering.add_features(df)

    df.to_csv(CLEAN_DATA_PATH, index=False)

    visualize.plot_hr_distribution(df)
    model.train_model(df)

if __name__ == "__main__":
    main()

