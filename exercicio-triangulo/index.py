from colorama import Fore, Style


def eh_triangulo(medida1, medida2, medida3, tipo_medida):
    if medida1 <= 0 or medida2 <= 0 or medida3 <= 0:
        return False
    elif (
        (medida1 + medida2 <= medida3 
        or medida1 + medida3 <= medida2 
        or medida2 + medida3 <= medida1)
        and tipo_medida == "l"
    ):
        return False
    else:
        return True
        
def classificacao_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 != lado2 != lado3:
        return "escaleno"
    else:
        return "isósceles"
    
def classificacao_angulo(angulo1, angulo2, angulo3):
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return "acutângulo"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return "retângulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        return "obtusângulo"
    
while True:
    opcao_continuar = input("Deseja verificar mais um triângulo?(S/N) ").lower()

    if opcao_continuar == "n":
        break
    elif opcao_continuar != "s":
        print(Fore.RED + f"{opcao_continuar}: opção inválida")
        print(Style.RESET_ALL)
        continue

    opcao_tipo_medida = input(
        "Deseja verificar o triângulo usando seus lados ou seus ângulos?(L/A) "
    ).lower()

    mostrar_tipo_angulo = False

    if opcao_tipo_medida != "a" and opcao_tipo_medida != "l":
        print(Fore.RED + f"{opcao_tipo_medida}: opção inválida")
        print(Style.RESET_ALL)
        continue
    elif opcao_tipo_medida == "a":
        opcao_mostrar_tipo_angulo = input(
            "Deseja mostrar a classificação de ângulo do triângulo?(S/N) "
        ).lower()

        if opcao_mostrar_tipo_angulo == "n":
            mostrar_tipo_angulo = False
        elif opcao_mostrar_tipo_angulo == "s":
            mostrar_tipo_angulo = True
        else:
            print(Fore.RED + f"{opcao_mostrar_tipo_angulo}: opção inválida")
            print(Style.RESET_ALL)
            continue

    nome_medida = "lado" if opcao_tipo_medida == "l" else "ângulo"

    medida1 = float(input(f"Qual a medida do primeiro {nome_medida}? "))
    medida2 = float(input(f"Qual a medida do segundo {nome_medida}? "))
    medida3 = float(input(f"Qual a medida do terceiro {nome_medida}? "))


    if eh_triangulo(medida1, medida2, medida3, opcao_tipo_medida):
        tipo_triangulo = classificacao_triangulo(medida1, medida2, medida3)

        if opcao_tipo_medida == "a" and mostrar_tipo_angulo:
            tipo_angulo = classificacao_angulo(medida1, medida2, medida3)
            
            print(
                Fore.GREEN 
                + f"Os {nome_medida}s inseridos caracterizam um triângulo {tipo_triangulo} e {tipo_angulo}"
            )
        else:
            print(
                Fore.GREEN 
                + f"Os {nome_medida}s inseridos caracterizam um triângulo {tipo_triangulo}"
            )
        print(Style.RESET_ALL)
    else:
        print(
            Fore.RED 
            + 
            f"Os {nome_medida}s inseridos são inválidos para um triângulo.\n- A soma de dois lados quaisquer deve ser maior que o lado restante\n- A soma dos três ângulos internos devem ser 180°, no qual nenhum ângulo pode ser 0°"
        )
        print(Style.RESET_ALL)
