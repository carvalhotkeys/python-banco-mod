class Conta:
    def __init__(self, num_conta, titular=''):
        self.__numc = int(num_conta)
        self.__titular = str(titular)
        self.__saldo = 0

    def getNumero(self):
        return self.__numc

    def setNumero(self, novo_num):
        self.__numc = novo_num
        return self.__numc

    def getTitular(self):
        return self.__titular

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, novosaldo):
        self.__saldo = novosaldo
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
        return valor

    def retirar(self, valor):
        if self.__saldo >= 0:
            self.__saldo = self.__saldo - valor
        else:
            self.__saldo = self.__saldo + valor
            self.__saldo = self.__saldo * -1
        return valor