def cal_primo(n):
    res = ''
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            res = 'não é primo'
        else:
            res = 'é primo'
    return res


numero = eval(input('Digite um número: '))
print(f'O número {numero}, {cal_primo(numero)}.')