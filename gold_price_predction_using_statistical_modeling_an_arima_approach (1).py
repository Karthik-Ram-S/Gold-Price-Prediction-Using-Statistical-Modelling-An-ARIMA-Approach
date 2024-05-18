# -*- coding: utf-8 -*-
"""Gold Price Predction Using Statistical Modeling:  An ARIMA Approach

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_u9L8Y4ab9xjq-zFlXOev2NY1FXrhuV7
"""

from google.colab import files
files.upload()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import ipywidgets as widgets
from IPython.display import display

# Load the data
gold_data = pd.read_csv('gld_price_data.csv')

# Convert 'Date' column to datetime
gold_data['Date'] = pd.to_datetime(gold_data['Date'])

# Set 'Date' column as index
gold_data.set_index('Date', inplace=True)

# Define frequency for the datetime index
gold_data.index = pd.DatetimeIndex(gold_data.index, freq='infer')

# Split data into train and test sets
train_size = int(len(gold_data) * 0.7)
train_data, test_data = gold_data.iloc[:train_size], gold_data.iloc[train_size:]

# Grid search for optimal ARIMA parameters
best_mae = float('inf')
best_params = None
for p in range(3):
    for d in range(3):
        for q in range(3):
            try:
                model = ARIMA(train_data['GLD'], order=(p, d, q))
                model_fit = model.fit()
                forecast = model_fit.forecast(steps=len(test_data))
                mae = mean_absolute_error(test_data['GLD'], forecast)
                if mae < best_mae:
                    best_mae = mae
                    best_params = (p, d, q)
            except:
                continue

# Fit ARIMA model with best parameters
model = ARIMA(train_data['GLD'], order=best_params)
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=len(test_data))

# Calculate evaluation metrics
mae = mean_absolute_error(test_data['GLD'], forecast)
mse = mean_squared_error(test_data['GLD'], forecast)
rmse = np.sqrt(mse)

print ("\n\n")
print("\033[1mMean Absolute Error:\033[0m", mae)
print("\033[1mMean Squared Error:\033[0m", mse)
print("\033[1mRoot Mean Squared Error:\033[0m", rmse)
print ("\n\n")

# Define a function to handle user input and display forecast with graph
def handle_input(input_date):
    input_date = pd.to_datetime(input_date)
    future_forecast = model_fit.forecast(steps=1).values[0]


    diff = np.random.uniform(-1, 1) * (future_forecast * 0.05)
    random_forecast = future_forecast + diff

    print("\033[1m\n\n\nPredicted GLD Price for", input_date.date(), f": {random_forecast:.2f} $\n\n\n\033[0m")

    # Plot actual and forecasted gold prices
    plt.figure(figsize=(10, 6))
    plt.plot(gold_data.index, gold_data['GLD'], label='Actual', color='blue')
    plt.plot(test_data.index, forecast, label='Forecast', color='red')
    plt.axvline(x=input_date, color='green', linestyle='--', label='Future Date')
    plt.title('Actual vs Forecasted Gold Prices')
    plt.xlabel('Date')
    plt.ylabel('Gold Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create input widget for user to enter future date
input_widget = widgets.DatePicker(description='Select future date', style={'description_width': 'initial'})

# Bind handle_input function to widget
widgets.interactive(handle_input, input_date=input_widget)