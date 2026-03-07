
class SaldoInsuficiente(Exception):
    def __init__(self, titular, saldo, valor):

        self.titular = titular

        self.saldo = saldo

        self.valor = valor  

        if isinstance(valor, (int, float)):


            super().__init__(
                f"Saldo insuficiente para '{titular}'"

                f"Tentou sacar R${valor:,.2f} | Saldo: R$ {saldo:,.2f}"
            )
        elif isinstance(valor,(str)):
            super().__init__(
                
                f"Saque recusado! O valor digitado \"{valor}\" não é um número."
            )
class ValorInvalido(Exception):
    def __init__(self, valor):

        if isinstance(valor, (int, float)):

            super().__init__(
            
                f"Valor inválido: R$ {valor}. O depósito deve ser maior que zero!"
            )
        elif isinstance(valor, str):
            
            super().__init__(
                f"O valor digitado \"{valor}\" não é um número!"
            )


class ContaNaoEncontrada(Exception):
    def __init__(self, numero_conta):
        super().__init__(
            f"Conta \"{numero_conta}\" não encotrada"
        )