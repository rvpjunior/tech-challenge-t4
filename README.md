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