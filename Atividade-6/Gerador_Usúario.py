"""
Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""

import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro se a resposta tiver status 4xx ou 5xx
        dados = resposta.json()

        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("Usuário gerado com sucesso:")
        print(f"Nome completo: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except KeyError:
        print("Erro ao interpretar os dados da API.")

# Executa a função
gerar_usuario()
