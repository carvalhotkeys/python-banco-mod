class AgenciaBancaria:
    def Agencia(self, num_agencia):
        self.__contas = []
        self.__num_agencia = int(num_agencia)
        return self.__num_agencia

    def getNumAgencia(self):
        return self.__num_agencia

    def addConta(self, num_conta):
        self.__contas.append(num_conta)
        return True

    def getConta(self, num_conta):
        for conta in self.__contas:
            if conta.getNumero() == num_conta:
                return conta
        return None

    def listContas(self):
        strContas =''
        for conta in self.__contas:
            strContas = strContas + f'Conta: {conta.getNumero()} Titular: {conta.getTitular():^25} Saldo: {conta.getSaldo():^15}' + '\n'
        return strContas