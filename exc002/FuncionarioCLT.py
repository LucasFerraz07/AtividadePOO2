from Funcionario import Funcionario

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario