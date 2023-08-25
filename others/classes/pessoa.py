
from datetime import date

ano_atual = int(str(date.today())[0:4])


class Pessoa:

    def __init__(self, nome, idade, ano_de_nascimento, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.ano_de_nascimento = ano_de_nascimento
        self.comendo = comendo
        self.falando = falando

    def falar(self):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo.')
        else:
            print(f'{self.nome} está falando.')
        self.falando = True

    def comer(self):
        if self.falando:
            print(f'{self.nome} não pode comer pois está falando.')
        else:
            print(f'{self.nome} está comendo.')
        self.comendo = True

    def parar_de_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer.')
        else:
            print(f'{self.nome} não está comendo.')
        self.comendo = False

    def parar_de_falar(self):
        if self.falando:
            print(f'{self.nome} parou de falar.')
        else:
            print(f'{self.nome} não está falando.')
        self.falando = False

    def saber_idade_pelo_ano_de_nascimento(self):
        idade_com_base_no_ano_de_nascimento = ano_atual - self.ano_de_nascimento
        print(f'A idade de {self.nome}, com base no ano de nascimento de seu é {idade_com_base_no_ano_de_nascimento}.')


if __name__ == '__main__':
    p1 = Pessoa('Mateus', 17, 2003)

    p1.comer()
    p1.falar()
    p1.parar_de_comer()
    p1.falar()
    p1.saber_idade_pelo_ano_de_nascimento()
