#!/usr/bin/python3

from datetime import datetime

name = input("What is your name?\n")
age = float(input("What is your age?\n"))

time = datetime.now().year

print(f"Hello, {name}. Your year of birth is {time - age}")