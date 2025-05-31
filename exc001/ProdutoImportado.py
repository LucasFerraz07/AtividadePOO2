from Produto import Produto

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxaImportacao):
        super().__init__(nome, preco, estoque)
        self.taxaImportacao = taxaImportacao

    def precoFinal(self, qntd):
        precoVenda = qntd * self.preco
        precoVenda += self.taxaImportacao
        return precoVenda
    
    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")
        print(f"Nome do produto: {self.nome}")
        print(f"Valor da compra: {self.preco}")
        print(f"Valor da taxa: {self.taxaImportacao}")
        print(f"Valor final da compra: {self.precoFinal()}")
        print("")