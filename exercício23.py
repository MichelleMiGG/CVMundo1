# Digitos.
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 10 % 100
m = n // 10 % 1000
print('Unidade: {}' .format(u))
print('Dízima: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))
