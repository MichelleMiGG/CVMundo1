# Viagem.
dist = int(input('Digite a distância da sua viagem em km: '))
if dist <= 200:
  pp = dist * 0.50
  print('A passagem custará R${}' .format(pp))
else:
  ppa = dist * 0.45
  print('A pasagem custará R${}' .format(ppa))
