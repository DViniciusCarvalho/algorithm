#!/usr/bin/python3

somatorio_salarios = 0
numero_salarios = 0
maior_salario = 0
menor_salario = 0

while True:
    opcao = input("Deseja cadastrar mais um funcionario?(S/N) ").lower()

    if opcao == "n":
        break

    salario = float(input("Qual o salário do funcionário? "))

    somatorio_salarios += salario
    numero_salarios += 1

    if salario > maior_salario:
        maior_salario = salario
    
    if menor_salario == 0 or salario < menor_salario:
        menor_salario = salario

print(f"O somatório dos salários é: {somatorio_salarios}")
print(f"A média salarial é: {somatorio_salarios / numero_salarios}")
print(f"O maior salário é: {maior_salario}")
print(f"O menor salário é: {menor_salario}")