class End_simples(object):

def __init__(self, rua, num, bairro):

       self.rua = rua

       self.num = num

       self.bai = bairro

def Endereco(self):

      return self.rua + ", " + self.num + "\ " + self.bairro

 class End_com(End_simples):

    def __init__(self, rua, num, bai, com):

        End_simples.__init__(self,rua, num, bairro):

        self.com = com

def Endereco(self):

...

a = End_simples("Av Brasil", "243", "Floresta")

b = End_com("Av Miracema", "12", "Centro", "apto 3")

print(a.Endereco())

print(b.Endereco())