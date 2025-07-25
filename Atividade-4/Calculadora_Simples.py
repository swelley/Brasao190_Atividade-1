"""
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
""" 
def calculadora():
    while True:
        try:
            # Solicita os dois números reais
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Solicita a operação desejada
            operacao = input("Escolha a operação (+, -, *, /): ").strip()

            # Verifica e realiza a operação
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break  # Sai do loop após operação válida

        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

# Executa a calculadora
calculadora()
