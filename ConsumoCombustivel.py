""""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
distancia_percorrida = 300
combustivel_gasto = 25
consumo_medio = distancia_percorrida / combustivel_gasto
print("Dados da Viagem:")
print("Distância percorrida: {} km".format(distancia_percorrida))
print("Combustível gasto: {} litros".format(combustivel_gasto))
print("Consumo médio: {:.0f} km/l".format(consumo_medio))   
