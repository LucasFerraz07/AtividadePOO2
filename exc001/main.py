from Produto import Produto
from ProdutoImportado import ProdutoImportado
from ProdutoNacional import ProdutoNacional

p = Produto("Teclado", 100.0, 20)
p2 = ProdutoImportado("Mouse", 20.5, 43, 7.34)
p3 = ProdutoNacional("Goiaba", 4.40, 28)

p.exibirDetalhes()
p2.exibirDetalhes()
p3.exibirDetalhes()

p2.vender(6)
p3.vender(8)

p3.repor(10)
