"""
Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""
import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        # A chave no JSON é sempre no formato moeda + "BRL", ex: "USDBRL"
        chave = f"{moeda.upper()}BRL"

        if chave not in dados:
            print("❌ Código da moeda inválido ou não encontrado.")
            return

        cotacao = dados[chave]

        # Extrair dados
        valor_atual = cotacao['bid']  # valor atual (bid)
        valor_max = cotacao['high']   # valor máximo
        valor_min = cotacao['low']    # valor mínimo
        timestamp = int(cotacao['timestamp'])

        # Converter timestamp para data/hora legível
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nCotação do {moeda.upper()} para BRL:")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Valor máximo: R$ {valor_max}")
        print(f"Valor mínimo: R$ {valor_min}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException as e:
        print("❌ Erro na conexão ou ao acessar a API:", e)
    except ValueError:
        print("❌ Erro ao processar os dados recebidos.")

if __name__ == "__main__":
    moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()
    consultar_cotacao(moeda_usuario)
