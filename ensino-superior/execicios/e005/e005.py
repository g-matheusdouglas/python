nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media > 7:
    r = 'Aprovado'
elif media >= 5:
    r = 'de Recuperação'
else:
    r = 'Reprovado'
print('A media do estudante foi {:4.4} e ele/ela está {}!'.format(media, r))
