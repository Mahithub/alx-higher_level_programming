#!/usr/bin/python3
"""Using the package Requests fetches https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    value = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(value.text)))
    print("    - content: {}".format(value.text))
