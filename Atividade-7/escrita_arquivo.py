""""
Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.

"""
import csv

# Lista de listas com dados fictícios: nome, idade e cidade
dados_pessoas = [
    ["Ana Silva", 28, "São Paulo"],
    ["Carlos Oliveira", 35, "Rio de Janeiro"],
    ["Mariana Souza", 22, "Belo Horizonte"]
]

def main():
    try:
        nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: pessoas.csv): ")

        # Abre o arquivo para escrita, modo texto
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)

            # Escreve o cabeçalho
            escritor_csv.writerow(["Nome", "Idade", "Cidade"])

            # Escreve os dados linha a linha
            for pessoa in dados_pessoas:
                escritor_csv.writerow(pessoa)

        print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao escrever o arquivo: {e}")

if __name__ == "__main__":
    main()
