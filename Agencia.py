from random import randint

class Agencia:

    def __init__(self,telefone,cnpj,numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa Atual: R${self.caixa:,.2f}')
        else:
            print(f'O valor de Caixa está ok. Caixa Atual: R${self.caixa:,.2f}')

    def emprestar_dinheiro(self,valor,cpf,juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
        else:
            print(f'Empréstimo não é Possível. Dinheiro não disponível em caixa')

    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self,site,telefone,cnpj):
        self.site = site
        ## super() = Rodar métodos da super Class
        super().__init__(telefone,cnpj,1000)
        self.caixa = 10000000
        self.caixa_paypal = 0

    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor


    def sacar_paypal(self,valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):

    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj)
        self.caixa = 10000


class AgenciaPreimum(Agencia):

    def __init__(self,telefone,cnpj):
        super().__init__(telefone,cnpj, numero=randint(1001,9999))
        self.caixa = 10000000

    def adicionar_cliente(self,nome,cpf,patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome,cpf,patrimonio)
        else:
            print('O cliente não tem patrimonio suficiente para entrar na Agencia')


agencia = Agencia(12345678,200000000000,4550)
agencia.caixa = 10000000000
agencia.verificar_caixa()

agencia.emprestar_dinheiro(15000,1111111111,0.05)
print(agencia.emprestimos)

agencia.adicionar_cliente('felipe',11111155511,15000000)
print(agencia.clientes)

agencia_virtual = AgenciaVirtual('www.teste.com',12345678,10545102450)
agencia_virtual.depositar_paypal(500000)
print(agencia_virtual.caixa)


agencia_premium = AgenciaPreimum(86123249,10101010101)
print(agencia_premium.caixa)
agencia_premium.adicionar_cliente('Felipe',11362076430,1000500)
print(agencia_premium.clientes)