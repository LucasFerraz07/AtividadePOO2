from Produto import Produto

class ProdutoNacional(Produto):
    pass

    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")
        print(f"Nome do produto: {self.nome}")
        print(f"Valor da compra: {self.preco}")
        print(f"Valor da taxa: 0")
        print(f"Valor final da compra: {self.precoFinal()}")
        print("")