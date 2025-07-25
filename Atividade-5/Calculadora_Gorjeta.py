"""
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Receba o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
* Exiba o valor total da conta com a gorjeta incluída.
* Exiba o valor da gorjeta com duas casas decimais.
"""
def calcular_conta_com_gorjeta(total, porcentagem):
    gorjeta = total * porcentagem / 100
    return gorjeta, total + gorjeta

# Solicita o valor da conta e a porcentagem da gorjeta
valor_conta = float(input("Digite o valor da conta: ").replace(",", "."))
porcentagem = float(
    input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): ").replace(",", ".")
)
# Calcula a gorjeta e o total com gorjeta
gorjeta, total_com_gorjeta = calcular_conta_com_gorjeta(valor_conta, porcentagem)

# Exibe os resultados formatados
print(
    f"Sua conta total com gorjeta fica: R$ {total_com_gorjeta:.2f} "
    f"(Gorjeta: R$ {gorjeta:.2f})"
)
