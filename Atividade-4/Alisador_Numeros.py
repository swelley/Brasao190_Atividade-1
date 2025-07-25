"""
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  
"""
def classificar_numeros():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if entrada.lower() == "fim":
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("Número par.")
                pares += 1
            else:
                print("Número ímpar.")
                impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executa a classificação de números
classificar_numeros()   