from Classes import Bola
from Classes import Quadrado
from Classes import Rectangulo
from Classes import Pessoa

novaBola = Bola("Amarela", 0.15, "borracha")
novaBola.mostraCor()
novaBola.trocaCor("Preta")
novaBola.mostraCor()

print("--" * 25)

novoQuadrado = Quadrado(2.50)
novoQuadrado.mostrarLado()
novoQuadrado.valorLado()
novoQuadrado.mostrarLado()
novoQuadrado.calcAreaQuad()

print("--" * 25)

novoRectangulo = Rectangulo(10, 5)
print(novoRectangulo.retornarValor())
novoRectangulo.mudarValor()
print(novoRectangulo.calcAreaRec())

print("--" * 25)

novaPessoa = Pessoa("Breno Lucena", 41, 1.79)
print(novaPessoa.envelhecer())
print(novaPessoa.engordar())
print(novaPessoa.emagrecer())
novaPessoa.crescer()