preco = 10.0
unidade = eval(input('Quantas unidades foram compradas: '))
desconto = 1
if 10 < unidade <= 20:
    desconto = 0.9
if unidade > 20:
    desconto = 0.8
valor = preco * unidade * desconto
print(f'O valor da compra é R${valor}.')