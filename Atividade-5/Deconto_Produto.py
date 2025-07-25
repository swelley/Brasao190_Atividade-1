"""
Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""
# Função lambda para calcular o desconto
calcular_desconto = lambda preco, percentual: preco - (preco * percentual / 100)

# Entrada de dados
preco_original = float(input("Digite o preço original do produto: ").replace(",", "."))
percentual_desconto = float(input("Digite o percentual de desconto (%): ").replace(",", "."))

# Cálculo
preco_final = calcular_desconto(preco_original, percentual_desconto)

# Saída formatada
print(f"O preço com desconto é: R$ {preco_final:.2f}")
print("Obrigado por usar nossa calculadora de desconto!")

