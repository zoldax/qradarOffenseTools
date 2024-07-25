# 🛠️ QRadar Offense Tools

This repository contains `qradarOffenseTools.py`, a Python script for fetching and displaying QRadar offenses. It provides options to output the data in CSV or JSON format and also allows users to display QRadar system information.

[![License](https://img.shields.io/github/license/zoldax/qradarOffenseTools?color=44CC11)](LICENSE)  [![Commit](https://img.shields.io/github/commit-activity/t/zoldax/qradarOffenseTools)](https://github.com/zoldax/qradarOffenseTools/commits/)  [![Views](https://hits.sh/github.com/zoldax/qradarOffenseTools.svg)](https://hits.sh/github.com/zoldax/qradarOffenseTools/) [![Last commit](https://img.shields.io/github/last-commit/zoldax/qradarOffenseTools/main)](https://github.com/zoldax/qradarOffenseTools/commits/main)

## 📖 Description
`qradarOffenseTools.py` is a command-line tool designed to interact with the QRadar API to retrieve and display offense data. The tool can output the data in both CSV and JSON formats for further analysis or reporting. Additionally, it can display QRadar system information.

## 🛠️ Usage
The script can be executed from the command line with various arguments to control its behavior.

### 1. Display QRadar Offenses
```python
python qradarOffenseTools.py --offense
```

### 2. Exporting Offenses to CSV
```python
python qradarOffenseTools.py --offense --format csv --output offenses.csv
```

### 3. Exporting Offenses to JSON
```python
python qradarOffenseTools.py --offense --format json --output offenses.json
```

### 4. Display QRadar System Information
```python
python qradarOffenseTools.py --version
```

## 📦 Requirements
- Python 3.6 or later
- Required Python packages:
  - argparse
  - csv
  - json
  - datetime
  - qradarzoldaxlib (custom library for QRadar interactions)

## 📥 Inputs
- Command-line arguments to control script behavior
- Configuration file: `config.txt`

## 📤 Outputs
- Console output for offenses and system information
- CSV or JSON files for exported offenses

## 🔑 Functionalities & Key Functions
- `get_offenses()`: Fetches offenses from QRadar API.
- `format_timestamp(epoch_millis)`: Converts epoch milliseconds to a human-readable datetime string.
- `print_offenses(offenses)`: Prints QRadar offenses to the console.
- `write_offenses_to_csv(offenses, filename)`: Writes offenses to a CSV file.
- `write_offenses_to_json(offenses, filename)`: Writes offenses to a JSON file.
- `print_qradar_version()`: Displays QRadar system information.

## 🛠 Configuration: config.txt
Configuration parameters required by the script:
1. `ip_QRadar`: IP address of the QRadar instance.
2. `auth`: Authentication token for QRadar API access.
3. `Version`: API version.
4. `Accept`: Accept header value.
5. `verify_ssl`: SSL verification (True/False).
6. `ssl_cert_path`: Path to SSL certificate.
7. `safety Parameter`: Additional safety parameters if any.

## 🔐 SSL API Connection Support
The script supports SSL API connections by configuring `verify_ssl` and `ssl_cert_path` in the `config.txt` file.

## 🚫 Error Handling
The script includes robust error handling mechanisms:
- Network request failures
- File I/O operations
- Timestamp conversion errors

Errors are logged using the configured logging level.

## 📝 Notes
- Ensure that the `config.txt` file is properly configured before running the script.
- The custom library `qradarzoldaxlib` must be available in the Python path.

## 📜 Disclaimer
This script is provided "as-is" without any warranties. Use it at your own risk. The authors and Abakus Sécurité are not responsible for any damage or data loss caused by the use of this script.

## License
Licensed under the Apache License, Version 2.0. See [LICENSE](http://www.apache.org/licenses/LICENSE-2.0) for more details.

