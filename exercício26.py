#  Letra A.
frase = str(input('Digite uma frase: ')).upper()
print('A letra A apaarece {} veazes na frase' .format(frase.count('A')))
print('A letra A parece na posição {} a primeira vez' .format(frase.find('A')+1))
print('A letra A aparece na posição {} a última vez' .format(frase.rfind('A')+1))
