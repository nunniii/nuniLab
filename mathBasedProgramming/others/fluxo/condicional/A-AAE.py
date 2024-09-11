class Usuario:
    def __init__(self, log):
        self.log = log
        if log:
            self.msg = "Usuário logado"
        else:
            self.msg = "Usuário deslogado"


print(Usuario(True).msg)