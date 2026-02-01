from time import sleep

alunos = []

def adicionar():
    nome = str(input('DIGITE O NOME DO ALUNO -> ')) 

    while True:
        idade = input('DIGITE A IDADE DO ALUNO -> ')
        if idade.isdigit()and int(idade) > 0:
            idade = int(idade)
            break
    else:
        print('IDADE INVÁLIDA !')
    
    while True:
        nota = input('DIGITE A NOTA DO ALUNO -> ')
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                break
            else:
                print('A NOTA DEVE SER ENTRE [0] E [10]')
        except ValueError:
            print('DIGITE UM NÚMERO VÁLIDO PARA A NOTA !')
    
    aluno = {"nome": nome, "idade": idade, "nota": nota}

    alunos.append(aluno)
    print(f'ALUNO [{nome}], ADICIONADO COM SUCESSO ✅\n')

def listar_alunos():
    if not alunos:
        print('NENHUM ALUNO REGISTRADO !')
    else:
        print('\nLISTA DE ALUNOS:')

        for idx, aluno in enumerate(alunos, start=1):
              print(f"{idx}. NOME: {aluno['nome']}, IDADE: {aluno['idade']}, NOTA: {aluno['nota']}")
              print('')


def buscar_aluno():
    nome_busca = input("DIGITE O NOME DO ALUNO PARA BUSCAR:").strip()
    encontrado = False
    for aluno in alunos:
            if aluno['nome'].lower() == nome_busca.lower():  
             print(f"ALUNO ENCONTRADO: NOME: [{aluno['nome']}], IDADE: [{aluno['idade']}], NOTA: [{aluno['nota']}]\n")
            encontrado = True
            break 
    if not encontrado:
        print('ALUNO NÃO ENCONTRADO !')
    
def remover_aluno():
    nome_remover = input('DIGITE O NOME DO ALUNO PARA REMOVER -> ').strip()
    for aluno in alunos:
         if aluno['nome'].lower() == nome_remover.lower():  
            alunos.remove(aluno)  
            print(f"Aluno {nome_remover} removido com sucesso! 🗑️\n")
            return  
    print("Aluno não encontrado!\n")

def media_geral():
    if not alunos:  
        print("Nenhum aluno cadastrado para calcular a média.\n")
        return
    soma = sum(aluno['nota'] for aluno in alunos)  
    media = soma / len(alunos)  
    print(f"A média geral das notas é: {media:.2f}\n")  


def menu():
    while True:  
        print("=== Sistema de Cadastro de Alunos ===")
        print("1 - Adicionar aluno")
        print("2 - Listar todos os alunos")
        print("3 - Buscar aluno pelo nome")
        print("4 - Remover aluno")
        print("5 - Mostrar média geral das notas")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip() 

        
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            media_geral()
        elif opcao == "6":
            print("Saindo do sistema... Até mais! 👋")
            break 
        else:
            print("Opção inválida! Tente novamente.\n")  

menu()
