while True:
    try:
        num = int(input('Digite um número interio: '))
        break
    except ValueError:
        print('Entre com um número válido')
print(f'O número digitado é {num}.')
