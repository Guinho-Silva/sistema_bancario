#Sistema de Conta Bancária
"""Crie um método de classe transferir(origem, destino, valor) que move dinheiro entre contas
Adicione um histórico de transações como lista
Lance exceções customizadas (SaldoInsuficienteError) em vez de só printar um aviso"""
# Um sistema simples de banco
from rich import print
from rich import inspect
from rich.panel import Panel
import datetime
from datetime import datetime

class ContaBancaria():
    def __init__(self, titular, saldo, numero_conta):

        # Atributos de instância

        self.titular = titular

        self.saldo = saldo

        self.numero_conta = numero_conta

        self.historico = []

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito

        self.historico.append({
            "Tipo": "Deposito",
            "Valor": valor_deposito,
            "Data": datetime.now()
        })

        return f"Deposito de {self.saldo} realizado com sucesso!"
    
    def sacar (self, valor_saque):  
        if valor_saque > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor_saque

        self.historico.append({
            "Tipo": "Saque",
            "Valor": valor_saque,
            "Data": datetime.now()
        })

        return f'Saque de {valor_saque} realizado com sucesso!'

    def extrato(self) -> str:
        conteudo = f'Titular: {self.titular}\n'

        conteudo += f"Número da Conta: {self.numero_conta}\n"

        if not self.historico:
            conteudo += f"Nenhuma movimentação realizada na conta: \'{self.numero_conta}\'\n"

        else:
            for movimentacao in self.historico:
                data_formatada = movimentacao["Data"].strftime("%d/%m/%Y %H:%M")

                conteudo += (
                    f"{data_formatada} | "
                    f"{movimentacao['Tipo']} | "
                    f"R$ {movimentacao['Valor']:.2f}\n"
                )

        conteudo += '-' *  56 + '\n'

        conteudo += f"Saldo atual: R${self.saldo:,.2f}"
        folha_extrato = Panel(conteudo, title="Extrato Bancário", width= 60)

        print(folha_extrato)
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, numero_conta, taxa_rendimento = 0.05):
        super().__init__(titular, saldo, numero_conta)

        self.taxa_rendimento = taxa_rendimento

    def aplica_rendimento(self):

        rendimento = self.saldo * self.taxa_rendimento

        self.saldo += rendimento
        return f'Rendimento aplicado: {rendimento}'
    
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, numero_conta, limite_cheque_especial):
        super().__init__(titular, saldo, numero_conta)

        self.limite_cheque_especial = limite_cheque_especial
    

    def sacar (self, valor):
        limite_total = self.saldo + self.limite_cheque_especial

        if valor > limite_total:
            print("Limite excedido.")
            return
        self.saldo -= valor
        print(f'Saque de R$ {valor:,.2f} realizado')



# -------REALIZANDO TESTES-------

# Efetuando testes dos atributos de instância usando a lib rich

# t1 = ContaBancaria('Iago', 1500, 123)

# teste do método depositar

# print(t1.depositar(1000))

# teste do método sacar

# print(t1.sacar(1500))

# Testa a classe ContaPoupanca e seus métodos

#t2 = ContaPoupanca('Iago', 1500, 123, taxa_rendimento= 0.05)
#print(t2.aplica_rendimento())

# t2.extrato()

# Testa a classe ContaCorrente e seu metodo

# t3 = ContaCorrente('Iago', 2500, 123, 4000)

# t3.sacar(8000)

# t3.extrato()