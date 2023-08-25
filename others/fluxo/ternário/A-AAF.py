Try = True
while Try:
    age = input('Informe sua idade: ')
    msg = 'Por gentileza, digite apenas números.' if not age.isnumeric() else 'Sua idade é {}.'.format(age)
    Try = True if not age.isnumeric() else False
    print(msg)
    print('Repetir: {}'.format('true' if Try == True else 'false'))
    del msg