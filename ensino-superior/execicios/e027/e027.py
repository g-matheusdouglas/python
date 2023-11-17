from sklearn.datasets import load_digits
digitos = load_digits()

#Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print('Shape dos dados de imagens:{}'.format(digitos.data.shape))
#Apresnata o total de daos rotulados com inteiros de 0 a 9
print('Shape dos daos rotulados: {}'.format(digitos.target.shape))
