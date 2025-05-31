class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome 
        self.preco = preco 
        self.estoque = estoque

    def exibirDetalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")
        print("")

    def precoFinal(self):
        return self.preco
    
    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")
        print(f"Nome do produto: {self.nome}")
        print(f"Valor da compra: {self.preco}")
        print(f"Valor da taxa: {self.taxaImportacao}")
        print(f"Valor final da compra: {self.preco}")
        print("")

    def vender(self, qntd):
        if self.estoque >= qntd:
            self.estoque -= qntd
            print(f"{qntd} {self.nome} vendidos!")
            print("")
            self.emitir_nota
        return self.estoque 
    
    def repor(self, qntd):
        self.estoque += qntd
        print(f"{qntd} {self.nome} adicionados ao estoque!")
        print("")
        return self.estoque 