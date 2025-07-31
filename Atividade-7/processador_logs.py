"""
Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos.
"""
import pandas as pd

def processar_logs():
    print("🔧 Iniciando processamento...")
    nome_arquivo = input("📁 Digite o nome do arquivo CSV: ").strip()

    try:
        df = pd.read_csv(nome_arquivo)

        if 'Tempo de Execucao' not in df.columns:
            print("❌ A coluna 'Tempo de Execucao' não foi encontrada no arquivo.")
            print(f"Colunas encontradas: {df.columns.tolist()}")
            return

        media = df['Tempo de Execucao'].mean()
        desvio = df['Tempo de Execucao'].std()

        print(f"📊 Média do tempo de execução dos tickets: {media:.2f} dias")
        print(f"📈 Desvio padrão: {desvio:.2f} dias")

    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado.")
    except pd.errors.EmptyDataError:
        print("❌ O arquivo está vazio ou mal formatado.")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

if __name__ == "__main__":
    processar_logs()
 
        