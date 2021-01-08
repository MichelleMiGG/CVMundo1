# Separando Nomes.
n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}' .format(nome[0]))
print('Seu último nome é {}' .format(nome[len(nome)-1]))
