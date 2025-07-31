"""
 Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

"""

import json
import os

def criar_dicionario():
    print("\nDigite os dados da pessoa:")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")

    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

def salvar_json(nome_arquivo, nova_pessoa):
    try:
        # Se o arquivo já existe, perguntar ao usuário
        if os.path.exists(nome_arquivo):
            escolha = input(f"\n⚠️ O arquivo '{nome_arquivo}' já existe. Deseja adicionar os dados a ele? (s/n): ").lower()
            if escolha == 's':
                with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                    try:
                        dados_existentes = json.load(arquivo)
                        if not isinstance(dados_existentes, list):
                            dados_existentes = [dados_existentes]
                    except json.JSONDecodeError:
                        dados_existentes = []
                dados_existentes.append(nova_pessoa)
            else:
                dados_existentes = [nova_pessoa]
        else:
            dados_existentes = [nova_pessoa]

        # Salvar no arquivo (sobrescreve com a nova lista completa)
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)

        print(f"\n✅ Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"\n❌ Erro ao salvar o arquivo: {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_lidos = json.load(arquivo)
            print("\n📄 Conteúdo atual do arquivo:")
            print(json.dumps(dados_lidos, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print(f"\n❌ Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"\n❌ Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
    except Exception as e:
        print(f"\n❌ Erro ao ler o arquivo: {e}")

def main():
    pessoa = criar_dicionario()
    nome_arquivo = input("\nDigite o nome do arquivo JSON (ex: pessoas.json): ")

    salvar_json(nome_arquivo, pessoa)
    ler_json(nome_arquivo)

if __name__ == "__main__":
    main()
