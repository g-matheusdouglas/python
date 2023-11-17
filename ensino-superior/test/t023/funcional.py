veiculos = ['avião', 'carro', 'navio', 'ônibus']

f_maiuscula = lambda x: str.upper(x)

nomes_maisculos = list(map(f_maiuscula, veiculos))

print(f'nomes maisculos = {nomes_maisculos}')
