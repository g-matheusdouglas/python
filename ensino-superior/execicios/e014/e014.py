def dividir(x, y):
    try:
        resultado = x / y
        print('A resposta é : ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero ')


dividir(3, 2)
dividir(3, 0)
