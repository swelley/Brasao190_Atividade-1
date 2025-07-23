"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""
def converter_temperatura(valor, origem, destino):
    # Converte a temperatura para Celsius
    if origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        celsius = valor

    # Converte de Celsius para a unidade de destino
    if destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return celsius

print("Conversor de Temperaturas")
valor = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").strip().upper()
destino = input("Digite a unidade de destino (C, F, K): ").strip().upper()

unidades_validas = ["C", "F", "K"]

if origem not in unidades_validas or destino not in unidades_validas:
    print("Unidade inválida. Use apenas C, F ou K.")
else:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"{valor}°{origem} é igual a {resultado:.2f}°{destino}")


