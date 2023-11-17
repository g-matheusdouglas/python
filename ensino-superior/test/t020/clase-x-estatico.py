from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Um método de classe par criar
    # Um objeto Pessao através do ano de nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    # Método Estático: verificar se é maior de idade.
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18


pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
# imprimir o resultado
print(Pessoa.ehMaiorIdade(pessoa1.idade))
