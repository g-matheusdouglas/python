from sklearn.tree import DecisionTreeClassifier, tree

lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]

resultado = [pera, pera, laranja, laranja]

#gerar um árvore de decisão

#classificador
clf = clf.fit(pomar, resultado)

peso = 140
# 1 para lisa e 0 para irregular
superficie = 1

resultado = clf.predict([[peso, superficie]])

if resultadousu == 1:
    print('Pera')
else:
    print('Laranja')
