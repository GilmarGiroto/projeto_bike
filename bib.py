from getpass import getpass
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.usuarios = []

    def criar_conta(self):
        print("Crie sua conta: ")
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu CPF: ")

        # Verifica se o CPF já está cadastrado
        for usuario in self.usuarios:
            if usuario['cpf'] == cpf:
                print("CPF já cadastrado, tente novamente!")
                return

        senha = getpass("Insira sua senha: ")
        senha_hash = sha256(senha.encode()).hexdigest()

        self.usuarios.append({'nome': nome, 'cpf': cpf, 'senha': senha_hash})
        print("Conta criada com sucesso!")

    def conectar_conta(self):
        print("Conecte-se à sua conta: ")

        cpf = input("Insira seu CPF: ")
        senha = getpass("Insira sua senha: ")
        senha_hash = sha256(senha.encode()).hexdigest()

        for usuario in self.usuarios:
            if usuario['cpf'] == cpf and usuario['senha'] == senha_hash:
                print("Conectado com sucesso!")
                print("Escolha seu plano de locação:")
                return

        print("Usuário ou senha inválidos, tente novamente.")

def mostrar_planos(planos_loc):
        print("Planos disponíveis:")
        for p in range(len(planos_loc)):
            print(planos_loc[p])

def escolha_plano():       
    while True:   
        escolha=int(input("Plano desejado: "))
        if escolha == 1:
            print("Plano Escolhido: Mensal - R$ 180,00")
            confirm=int(input("Digite '1' para confirmar plano ou '2' para alterar: "))
            if confirm == 1:
                print("Plano mensal confirmado")
                break           
            else:
                pass
        elif escolha == 2:
            print("Plano Escolhido: Quinzenal - R$ 90,00")
            confirm=int(input("Digite '1' para confirmar plano ou '2' para alterar: "))
            if confirm == 1:
                print("Plano Quinzenal confirmado")
                break
            else:
                pass
                
        elif escolha == 3:
            print("Plano Escolhido: Semanal - R$ 45,00")
            confirm=int(input("Digite '1' para confirmar plano ou '2' para alterar: "))
            if confirm == 1:
                print("Plano Semanal confirmado")
                break
            else:
                pass
        elif escolha == 0:
            print("OFunção finalizada!")
            break
        
        else:
            print("Não identificamos sua escolha, tente novamente.")
