# Aluguel de carros.
dia = int(input('Quantos dias você quer alugar o carro?'))
km = float(input('Quantos quilômetros você vai andar?'))
aluguel = (60 * dia) + (km * 0.15)
print('Por {} dias e por {} km rodado, você pagará {}' .format(dia, km, aluguel))
