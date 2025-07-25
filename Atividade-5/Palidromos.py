"""
Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.
"""
def eh_palindromo(frase):
    # Remove espaços, acentos e pontuação
    frase = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
    # Verifica se a frase é igual ao seu reverso
    return frase == frase[::-1]

# Solicita ao usuário uma palavra ou frase
entrada = input("Digite uma palavra ou frase: ")

# Verifica se é palíndromo
if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")    

