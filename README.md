# Tech Challenge Term 4

This project focuses on developing a model to predict the stock values of a company.

## Scripts

### Extract data to CSV

To extract the data to a CSV file, run the following commands:

```sh

cd extract_data/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py --company <company> --start <start_year> --end <end_year>
```

Replace `<company>`, `<start_year>`, and `<end_year>` with the desired values. The generated CSV file will be located in the `/extract_data` folder.