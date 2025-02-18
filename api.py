from flask import Flask, request, jsonify
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = load_model('google_prediction_model.keras')

# Define the min and max values for normalization
min_close = 10.873247146606444
max_close = 196.66000366210935

max_high = 2.01419998e+02
min_high = 11.02808943

max_low = 1.94979996e+02
min_low = 10.81240584

max_open = 1.97250000e+02
min_open = 10.92909997

max_volume = 5.92399008e+08
min_volume = 9312000

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'date' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    COMPANY = "GOOGL"
    date_str = data['date']

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

    # Get the 30 calendar days before the specified date
    start_date = date - timedelta(days=30)
    end_date = date

    # Fetch the stock data using yfinance
    stock_data = yf.download(COMPANY, start=start_date, end=end_date, multi_level_index=False)

    stock_data = stock_data.tail(15)  # Get the last 15 items
    if len(stock_data) < 15:
        return jsonify({'error': 'Insufficient stock data for the last 15 business days'}), 400

    stock_data.reset_index(inplace=True)
    stock_data.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    required_columns = ['Close', 'High', 'Low', 'Open', 'Volume']

    # Normalize the data
    stock_data["Close"] = (stock_data["Close"] - min_close) / (max_close - min_close)
    stock_data["High"] = (stock_data["High"] - min_high) / (max_high - min_high)
    stock_data["Low"] = (stock_data["Low"] - min_low) / (max_low - min_low)
    stock_data["Open"] = (stock_data["Open"] - min_open) / (max_open - min_open)
    stock_data["Volume"] = (stock_data["Volume"] - min_volume) / (max_volume - min_volume)

    # Prepare the input data for prediction
    stock_data_values = stock_data[required_columns].to_numpy()
    stock_data_values = np.expand_dims(stock_data_values, axis=0)
    
    # Make the prediction
    prediction = model.predict(stock_data_values)

    # Denormalize the prediction
    denormalized_prediction = float(prediction[0][0] * (max_close - min_close) + min_close)

    return jsonify({'predicted_close_price': denormalized_prediction})

if __name__ == '__main__':
    app.run(debug=True)