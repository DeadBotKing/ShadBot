import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


class MarketAnalysisModule:
    def __init__(self, data):
        self.data = data

    def preprocess_data(self):
        # Fill missing values with the median of each column
        self.data.fillna(self.data.median(), inplace=True)

        # Convert categorical variables to numerical
        self.data = pd.get_dummies(self.data)

    def split_data(self, test_size=0.2):
        X = self.data.drop(
            "target", axis=1
        )  # Assuming 'target' is the column we want to predict
        y = self.data["target"]

        return train_test_split(X, y, test_size=test_size, random_state=42)

    def train_model(self, X_train, y_train):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse

    def predict(self, new_data):
        new_data.fillna(new_data.median(), inplace=True)
        new_data = pd.get_dummies(new_data)

        # Ensure the new data has the same features as the training data
        required_features = set(self.data.columns) - {"target"}
        for feature in required_features:
            if feature not in new_data.columns:
                new_data[feature] = 0

        return self.model.predict(new_data)


# Example usage
if __name__ == "__main__":
    # Load and preprocess data
    data = pd.read_csv("market_data.csv")

    module = MarketAnalysisModule(data)
    module.preprocess_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = module.split_data()

    # Train the model
    module.train_model(X_train, y_train)

    # Evaluate the model
    mse = module.evaluate_model(X_test, y_test)
    print(f"Mean Squared Error: {mse}")

    # Make predictions
    new_data = pd.DataFrame({"feature1": [0.5], "feature2": [1.0]})
    prediction = module.predict(new_data)
    print(f"Predicted Value: {prediction[0]}")
