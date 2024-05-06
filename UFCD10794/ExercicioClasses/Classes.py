import math
from datetime import date

class Bola:
    def __init__(self, cor: str, circun: float, material: str):
        self.cor = cor
        self.circun = circun
        self.material = material

    def trocaCor(self, novaCor: str):
        self.cor = novaCor
        #return self.cor

    def mostraCor(self):
        print(f"A cor da bola é {self.cor}")

    def calcCircunf(self, raio: float):
        return 2 * math.pi * raio

class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def valorLado(self):
        self.lado = float(input("Digite o novo valor do lado: "))

    def mostrarLado(self):
        print(f"O lado é: {self.lado}")

    def calcAreaQuad(self):
        area = math.pow(self.lado, 2)
        print(f"A área do quadrado é {area}")

class Rectangulo:
    def __init__(self, ladoA: float, ladoB: float):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValor(self):
        self.ladoA = float(input("Digite o novo valor para o ladoA: "))
        self.ladoB = float(input("Digite o novo valor para o ladoB: "))

    def retornarValor(self):
        return f"Valor do ladoA: {self.ladoA}\nValor do ladoB: {self.ladoB}"

    def calcAreaRec(self):
        return f"A área do rectangulo é: {self.ladoA * self.ladoB:0.2f}"

class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def envelhecer(self):
        mesNascimento = int(input("Digite o mes de nascimento: "))
        if mesNascimento > date.today().month:
            self.idade += 1
            return f"Você tem {self.idade} e está mais velho"
        else:
            return f"Faltam {date.today().month - mesNascimento} meses para ficar mais velho"

    def engordar(self):
        pesoIdeal = 52 + (0.75 * (self.altura - 152.40))
        pesoAtual = (float(input("Digite seu peso atual: ")))
        if pesoAtual < pesoIdeal:
            return f"Utilizador precisa engordar {pesoIdeal - pesoAtual}kg para chegar ao peso ideal de {pesoIdeal}kg"
        elif pesoAtual == pesoIdeal:
            return f"Você está no peso ideal de {pesoIdeal}"
        else:
            return "Você precisa emagrecer"

    def emagrecer(self):
        pesoIdeal = float(52 - 0.75 * (152.40 - self.altura))
        pesoAtual = (float(input("Digite seu peso atual: ")))
        if pesoAtual > pesoIdeal:
            return f"Utilizador precisa emagrecer {(pesoAtual - pesoIdeal) * 0.25 + pesoIdeal:0.2f}kg para chegar ao peso ideal de {pesoIdeal:0.2f}kg"
        elif pesoAtual == pesoIdeal:
            return f"Você está no peso ideal de {pesoIdeal}"
        else:
            return "Você precisa emagrecer"

    def crescer(self):
        if self.idade < 21:
            conta = self.idade
            alturaFinal = self.altura
            while conta <= 21:
                alturaFinal += 0.5
                conta += 1
            print(f"Sua altura final será {alturaFinal}")
        else:
            print(f"Você já tem mais de 21 anos. Só consegue crescer para os lados. :D")