#!/bin/bash
# For a given URL, get the size of the HTTP response in byte

curl -s "$1" | wc -c
