from sklearn.linear_model import LinearRegression

def train_model(df):
    """
    Function to train a simple model (e.g., Linear Regression for home run prediction).
    """
    X = df[['ab', 'slg', 'obp']]  # Features
    y = df['hr']  # Target

    model = LinearRegression()
    model.fit(X, y)

    # Store the trained model (for simplicity, we can just return it here)
    return model

