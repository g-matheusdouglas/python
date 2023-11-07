# Função 01
def e_par(n):
    r = n % 2 == 0
    return r


# Função 02
def soma_par(lista):
    soma = 0
    for num in lista:
        if e_par(num):
            soma += num
    return soma


# Programa
lista_numeros = [3, 8, 6, 5, 2, 9, 1, 4, 10]
soma = soma_par(lista_numeros)
print(f'A soma dos números pares da lista é {soma}')
