from sklearn.datasets import load_digits
digitos = load_digits()

#Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print('Shape dos dados de imagens:{}'.format(digitos.data.shape))
#Apresnata o total de daos rotulados com inteiros de 0 a 9
print('Shape dos daos rotulados: {}'.format(digitos.target.shape))


import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 4))
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5],
                                             digitos.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(imagem, (8, 8)),
               cmap=plt.cm.gray)
    plt.title('Treinamento: {}\n'.format(rotulo, fontsize = 15))