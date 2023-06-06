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

