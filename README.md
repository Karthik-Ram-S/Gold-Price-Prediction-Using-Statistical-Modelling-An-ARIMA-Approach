# Gold Price Prediction Using Statistical Modeling: An ARIMA Approach

This project demonstrates the use of ARIMA (AutoRegressive Integrated Moving Average) modeling to predict the price of gold. The notebook is developed using Google Colab and includes data pre-processing, model training, hyperparameter tuning, and visualization of the results.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling](#modeling)
- [Results](#results)
- [Contributing](#contributing)

## Overview

The goal of this project is to build a statistical model to predict gold prices using historical data. We use the ARIMA model due to its efficacy in time series forecasting. The project involves:

- Loading and pre-processing the data.
- Splitting the data into training and testing sets.
- Performing a grid search to find the best ARIMA parameters.
- Evaluating the model using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
- Visualizing the actual and predicted gold prices.
- Allowing user input to predict future gold prices on a specific date.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Karthik-Ram-S/Gold-Price-Prediction-Using-Statistical-Modelling-An-ARIMA-Approach.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Gold-Price-Prediction-Using-Statistical-Modelling-An-ARIMA-Approach
    ```
3. Install the required dependencies:
    ```sh
    pip install numpy pandas matplotlib statsmodels scikit-learn ipywidgets
    ```

## Usage

1. Upload the gold price data file (`gld_price_data.csv`) using Google Colab's file upload functionality.
2. Run the notebook cells sequentially to load the data, fit the model, and make predictions.
3. Use the interactive widget to input a future date and visualize the predicted gold price.

## Modeling

The ARIMA model is used for predicting the gold prices. Here are the steps involved:

1. **Data Loading and Pre-processing**:
    - Convert the 'Date' column to datetime format.
    - Set the 'Date' column as the index.
    - Define the frequency for the datetime index.

2. **Train-Test Split**:
    - Split the data into training (70%) and testing (30%) sets.

3. **Grid Search for Optimal ARIMA Parameters**:
    - Iterate over a range of values for ARIMA parameters (p, d, q).
    - Fit the model for each combination of parameters and compute the Mean Absolute Error (MAE).
    - Select the combination of parameters that results in the lowest MAE.

4. **Model Fitting and Forecasting**:
    - Fit the ARIMA model with the best parameters.
    - Forecast the gold prices for the test data period.
    - Compute evaluation metrics: MAE, MSE, RMSE.

5. **User Input for Future Predictions**:
    - Use an interactive widget to input a future date.
    - Display the predicted gold price for the selected date.
    - Visualize the actual and predicted gold prices.

## Results

The model's performance is evaluated using the following metrics:

- **Mean Absolute Error (MAE)**: 4.888048433102212
- **Mean Squared Error (MSE)**: 41.70231713884276
- **Root Mean Squared Error (RMSE)**: 6.457733126944993

The notebook provides a plot that compares the actual gold prices with the predicted values for the test period.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
