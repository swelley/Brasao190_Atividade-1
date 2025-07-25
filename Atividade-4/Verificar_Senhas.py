""""
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""
def verificar_senha():
    while True:
        senha = input("Digite a senha (ou 'sair' para encerrar): ")
        if senha.lower() == "sair":
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue

        if not any(char.isdigit() for char in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue

        print("Senha forte.")
        break

# Executa a verificação de senha
verificar_senha()       