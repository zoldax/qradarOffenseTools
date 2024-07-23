#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
qradarOffenseTools.py

Copyright 2024 Pascal Weber (zoldax) / Abakus Sécurité

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Description:
    This script fetches and displays QRadar offenses, providing options
    to output the data in CSV or JSON format. It also allows users to 
    display QRadar system information. The script is designed to be 
    executed from the command line with various arguments to control its 
    behavior.

Usage:
    python qradarOffenseTools.py [OPTIONS]

Options:
    --offense              Display QRadar offenses.
    --version              Display QRadar system information.
    --format [csv|json]    Output format for offenses (csv or json).
    --output FILE          Output file name for offenses.

Examples:
    python qradarOffenseTools.py --offense
    python qradarOffenseTools.py --offense --format csv --output offenses.csv
    python qradarOffenseTools.py --version
"""

import argparse
import csv
import json
from datetime import datetime
from qradarzoldaxlib import make_request, print_qradar_version, read_config, logger

# Ensure config is read
config = read_config()

def get_offenses():
    """
    Fetch the offenses from the `/siem/offenses` API endpoint in QRadar.

    Returns:
        dict: JSON response as a dictionary containing offenses if successful,
              empty dictionary otherwise.
    """
    url = f"https://{config['ip_QRadar']}/api/siem/offenses"
    return make_request(url)

def format_timestamp(epoch_millis):
    """
    Convert epoch milliseconds to a human-readable datetime string.

    Args:
        epoch_millis (int): The epoch time in milliseconds.

    Returns:
        str: Formatted datetime string.
    """
    return datetime.fromtimestamp(epoch_millis / 1000).strftime('%Y-%m-%d %H:%M:%S')

def print_offenses(offenses):
    """
    Print QRadar offenses to the console.

    Args:
        offenses (list): List of offenses dictionaries.
    """
    print("QRadar Offenses:")
    if offenses:
        for offense in offenses:
            print(f"""
ID: {offense.get('id', 'N/A')}
Description: {offense.get('description', 'N/A')}
Credibility: {offense.get('credibility', 'N/A')}
Categories: {', '.join(offense.get('categories', []))}
Magnitude: {offense.get('magnitude', 'N/A')}
Start Time: {format_timestamp(offense.get('start_time')) if offense.get('start_time') else 'N/A'}
Status: {offense.get('status', 'N/A')}
Closing User: {offense.get('closing_user', 'N/A')}
Inactive: {offense.get('inactive', 'N/A')}
Last Updated Time: {format_timestamp(offense.get('last_updated_time')) if offense.get('last_updated_time') else 'N/A'}
            """)
    else:
        print("No offenses found or error occurred while fetching offenses.")

def write_offenses_to_csv(offenses, filename):
    """
    Write QRadar offenses to a CSV file.

    Args:
        offenses (list): List of offenses dictionaries.
        filename (str): The name of the output CSV file.
    """
    keys = offenses[0].keys() if offenses else []
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(offenses)

def write_offenses_to_json(offenses, filename):
    """
    Write QRadar offenses to a JSON file.

    Args:
        offenses (list): List of offenses dictionaries.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w') as jsonfile:
        json.dump(offenses, jsonfile, indent=4)

def main():
    """
    Main function to parse arguments and initiate the display or export of QRadar offenses.
    """
    parser = argparse.ArgumentParser(description="Display QRadar offenses and system info by Abakus Sécurité / Pascal Weber (zoldax).")
    parser.add_argument('--offense', action='store_true', help='Display QRadar offenses')
    parser.add_argument('--version', action='store_true', help='Display QRadar system information')
    parser.add_argument('--format', choices=['csv', 'json'], help='Output format for offenses')
    parser.add_argument('--output', type=str, help='Output file name for offenses')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.offense:
        offenses = get_offenses()
        print_offenses(offenses)
        if args.format and args.output:
            if args.format == 'csv':
                write_offenses_to_csv(offenses, args.output)
            elif args.format == 'json':
                write_offenses_to_json(offenses, args.output)

    if args.version:
        print_qradar_version()

if __name__ == "__main__":
    main()

