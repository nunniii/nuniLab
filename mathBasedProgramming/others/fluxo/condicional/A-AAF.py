Try = True
while Try:
    age = input('Informe sua idade: ')
    if not age.isnumeric():
        msg = 'Por gentileza, digite apenas números.'
        Try = True
    else:
        msg = 'Sua idade é {}.'.format(age)
        Try = False
    print(msg)
    if Try == True:
        msg2 = 'true'
    else:
        msg2 = 'false'
    print('Repetir: {}'.format(msg2))
    del msg , msg2