"""
Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
""" 
from datetime import date

# Ano atual automático
ano_atual = date.today().year

# Entrada do usuário
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

# Cálculo usando lambda (1 ano = 365 dias, sem considerar anos bissextos)
calcular_idade_dias = lambda nasc, atual: (atual - nasc) * 365

idade_dias = calcular_idade_dias(ano_nascimento, ano_atual)

print(f"Sua idade aproximada em dias é: {idade_dias} dias.")
# Fim do código