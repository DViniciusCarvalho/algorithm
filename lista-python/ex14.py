#!/usr/bin/python3

price = 80

discount = float(input(
    f"The product costs ${price}, how much discount do you want in percentage?\n"
))

decimal_discount = discount / 100
new_price = (1 - decimal_discount) * price

print(f"The new price is: ${new_price}")