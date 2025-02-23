import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta

def convert_date_to_number(date):
    """Converts a date string (YYYY-MM-DD) to the number of days since 1970-01-01."""
    return (datetime.strptime(date, "%Y-%m-%d") - datetime(1970, 1, 1)).days

def prepare_data(date_list, value_list):
    """Converts dates to numerical values and scales the data."""
    X = np.array([convert_date_to_number(date) for date in date_list]).reshape(-1, 1)
    y = np.array(value_list)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X, y, X_scaled, scaler

class DateValuePredictor:
    """Predicts values based on dates using linear regression."""

    def __init__(self):
        self.model = LinearRegression()
        self.scaler = None
        self.trained = False

    def train(self, date_list, value_list):
        """Trains the model with the given data."""
        X, y, X_scaled, scaler = prepare_data(date_list, value_list)
        self.model.fit(X_scaled, y)
        self.scaler = scaler
        self.trained = True

    def predict(self, date):
        """Predicts the value for a given date."""
        if not self.trained:
            raise Exception("The model has not been trained yet.")

        X_pred = np.array([convert_date_to_number(date)]).reshape(-1, 1)
        X_pred_scaled = self.scaler.transform(X_pred)
        predicted_value = self.model.predict(X_pred_scaled)[0]
        return predicted_value

    def plot(self, date_list, value_list):
        """Plots the actual data and the regression line."""
        if not self.trained:
            raise Exception("The model has not been trained yet.")

        X, y, X_scaled, _ = prepare_data(date_list, value_list)

        # Convert X back to datetime objects
        X_datetime = [datetime(1970, 1, 1) + timedelta(days=int(x[0])) for x in X]

        plt.scatter(X_datetime, y, color='blue', label='Dados Reais')
        plt.plot(X_datetime, self.model.predict(X_scaled), color='red', label='Linha de Regressão')
        plt.xlabel("Data")
        plt.ylabel("Valor")
        plt.legend()
        plt.gcf().autofmt_xdate()  # Rotate x-axis labels for better readability
        plt.show()

# Exemplo de uso
if __name__ == "__main__":
    predictor = DateValuePredictor()
    date_list = []
    value_list = []
    with open("csv/teste.csv", "r") as file:
        for value in file:
            value = value[:10]
            date_list.append(value)
            
    with open("csv/valorteste.csv", "r") as file:
        for value in file:
            value = value[:-2]
            value_list.append(value)
    print(value_list)

    predictor.train(date_list, value_list)
    predictor.plot(date_list, value_list)

    # Fazendo a previsão
    future_date = "2025-12-12" 
    predicted_value = predictor.predict(future_date)
    print(f"Valor previsto para {future_date}: {predicted_value:.2f}")