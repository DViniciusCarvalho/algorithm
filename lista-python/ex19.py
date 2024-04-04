#!/usr/bin/python3

from math import pi

radius = float(input("What is the cylinder radius?\n"))
height = float(input("What is the cylinder height?\n"))

volume = pi * (radius ** 2) * height

print(f"The cylinder volume is: {volume}")