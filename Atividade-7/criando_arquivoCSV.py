#
import csv

import csv

def coletar_tickets():
    tickets = []
    print("Digite os dados de 3 tickets:")

    for i in range(3):
        print(f"\nTicket {i + 1}:")
        ticket_id = input("ID do Ticket: ")
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        status = input("Status (ex: aberto, em andamento, resolvido): ")
        tickets.append([ticket_id, titulo, descricao, status])
    
    return tickets

def salvar_csv(nome_arquivo, tickets):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["ID", "Título", "Descrição", "Status"])  # Cabeçalho
            escritor.writerows(tickets)
        
        print(f"\n✅ Tickets gravados com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"\n❌ Erro ao escrever o arquivo: {e}")

def main():
    tickets = coletar_tickets()
    nome_arquivo = input("\nDigite o nome do arquivo CSV para salvar os tickets : ")
    salvar_csv(nome_arquivo, tickets)

if __name__ == "__main__":
    main()

