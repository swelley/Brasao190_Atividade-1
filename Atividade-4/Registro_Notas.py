""""
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.
"""
def registrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ")
        if entrada.lower() == "fim":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(notas)}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Executa o registro de notas
registrar_notas()