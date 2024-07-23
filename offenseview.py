#!/usr/bin/env python3

"""
   offenseview.py

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

"""

import argparse
from qradarzoldaxlib import make_request, print_qradar_version

def get_offenses() -> dict:
    """
    Fetch the offenses from the `/siem/offenses` API endpoint in QRadar.

    :return: JSON response as a dict containing offenses if successful,
             empty dict otherwise.
    """
    url = f"https://{config['ip_QRadar']}/siem/offenses"
    return make_request(url)

def print_offenses():
    """Retrieve and print QRadar offenses."""
    offenses = get_offenses()
    print("QRadar Offenses:")
    if offenses:
        for offense in offenses:
            print(f"ID: {offense.get('id', 'N/A')}, Description: {offense.get('description', 'N/A')}")
    else:
        print("No offenses found or error occurred while fetching offenses.")

def main():
    parser = argparse.ArgumentParser(description="Display QRadar offenses and system info.")
    parser.add_argument('--offense', action='store_true', help='Display QRadar offenses')
    parser.add_argument('--version', action='store_true', help='Display QRadar system information')

    args = parser.parse_args()

    if args.offense:
        print_offenses()
    if args.version:
        print_qradar_version()

if __name__ == "__main__":
    main()

