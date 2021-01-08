# Nome Completo.
nome = str(input('Digite seu nome completo: '))
print('O nome em maiúscula é {}' .format(nome.upper()))
print('O nome em minúsculas é {}' .format(nome.lower()))
print('O nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
