# Tech Challenge Term 4

This project focuses on developing a model to predict the stock values of a company.

## Scripts

### Setup

Set up the environment and install the dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Extract data to CSV

To extract the data to a CSV file, run the following command:

```sh
python extract_data.py --company <company> --start <start_year> --end <end_year>
```

Replace `<company>`, `<start_year>`, and `<end_year>` with the desired values.

### Analyze the data

To visualize and analyze the data behaviour, run the `analyze_data` notebook.

You must replace the `FILE_PATH` value with the data file path.

### Train the model

Run the notebook to train the model and it will be saved in `google_prediction_model.keras` file.

## API

The API allows users to interact with the stock prediction model programmatically. It provides endpoints to predict stock values based on the trained model.

### Setup

Set up the environment, install the dependencies and run the API:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 api.py
```

It will start the API in `http://localhost:5000`.

### Documentation

#### POST /api/predict
- **Description**: Predicts the stock value for a given date.
- **Parameters**: 
    - JSON object with the following field:
        - `date` (string): The date for which to predict the stock value in `YYYY-MM-DD` format
- **Response**: JSON object with the predicted stock value

#### Example: Predict stock value

Request:
```sh
curl -X POST http://localhost:5000/api/predict -H "Content-Type: application/json" -d '{
    "date": "2023-10-01"
}'
```

Response:
```json
{
    "predicted_close_price": 150.25
}
```