class Usuario:
    def __init__(self, log):
        self.log = log
        self.msg = 'Usuário logado.' if log else 'Usuário deslogado.'

print(Usuario(True).msg)