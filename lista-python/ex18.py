#!/usr/bin/python3

tax_rate = 0.1

salary = float(input("What is your salary in dollars?\n"))

liquid_salary = (1 - tax_rate) * salary

print(f"Your liquid salary is: ${liquid_salary}")