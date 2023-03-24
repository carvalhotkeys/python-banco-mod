from ClassConta import Conta
from ClassAgencia import AgenciaBancaria

Banco = AgenciaBancaria()  #cria classe agencia bancaria
Banco.Agencia(333)         #cria numero da agencia

C = Conta(311, 'Pedro Henrique')
C.setSaldo(6010)
Banco.addConta(C)
C = Conta(421, 'Maria Jose Ferreira')
C.depositar(500)
Banco.addConta(C)
C = Conta(522, 'Jessica Malao Josoares')
C.retirar(220)
Banco.addConta(C)
Banco.addConta(Conta(511, "Jusefina Parangaba"))

print('---------------------', 'BANCO CARVSCRED', '-------------------------')
print('--------------------- AGENCIA:', Banco.getNumAgencia(), '----------------------------')
print()
print(Banco.listContas())
print()
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

perguntaD = str(input('Você deseja cadastrar mais alguem? ')).strip().upper()[0]
if perguntaD == 'S':
    pergunta = int(input('Quantas contas deseja cadastrar? '))
    for i in range(1, pergunta + 1):
        conta = int(input('Digite o numero da conta: '))
        titular = str(input('Digite o nome do titular: '))
        C = Conta(conta, titular)
        Banco.addConta(C)
    print('---------------------', 'BANCO CARVSCRED', '-------------------------')
    print('--------------------- AGENCIA:', Banco.getNumAgencia(), '----------------------------')
    print()
    print(Banco.listContas())
    print()
    print('---------------------------------------------------------------')
    print('---------------------------------------------------------------')
else:
    print('Obrigado Até Logo..')