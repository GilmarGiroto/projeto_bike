from bib import *

usuario = Usuario()

while True:
    print("Selecione uma opção:")
    print("1. Criar uma conta")
    print("2. Conectar-se à conta")
    print("3. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        usuario.criar_conta()

        with open('usuarios.txt', 'a') as arquivo:
            for usr in usuario.usuarios:
                try:
                    arquivo.write(f"Nome: {usr['nome']}\n")
                    arquivo.write(f"CPF: {usr['cpf']}\n")
                    arquivo.write(f"Senha: {usr['senha']}\n")
                    arquivo.write("\n")
                except Exception as e:
                    print(f"Erro ao escrever no arquivo: {str(e)}")

    elif opcao == "2":
        usuario.conectar_conta()
    elif opcao == "3":
        print("Obrigado por utilizar o programa!")
        break
    else:
        print("Opção inválida, tente novamente.")
