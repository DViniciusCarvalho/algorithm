#!/usr/bin/python3

rate = float(input("What is the exchange rate of dollar in brazilian real?\n"))
amount = float(input("How many dollars do you want to convert?\n"))

real = rate * amount

print(f"The amount in Brazilian reals is: {real}")