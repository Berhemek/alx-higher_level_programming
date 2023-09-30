#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
except urllib.error.HTTPError as e:
    print(f"Error: {e.code} {e.reason}")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")

