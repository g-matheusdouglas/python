def cal_fatorial(numero):
    num = numero - 1
    f = numero
    for i in range(numero):
        if num != 0:
            f *= num
            print(f)
        num -= 1
        i += 1
    return f

n = eval(input('Digite um numero: '))
n_fatorial = cal_fatorial(n)
print(f'O fatorial de um é {n_fatorial}.')