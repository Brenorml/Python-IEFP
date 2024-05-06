from dataclasses import dataclass

@dataclass #Versão simplificada da classe ex: o constructor não é preciso declarar
class Morada:
    rua: str
    num: str
    apt: str
    cp: int

    def get_cp_formatado(self):
        cp_str = str(self.cp)
        cp_formatado = f"{cp_str[:4]}-{cp_str[4:]}"
        return cp_formatado
class Morada2: #Falta o constructor, quando instanciada vai dar erro
    rua: str
    num: str
    apt: str
    cp: int

class Morada3: #Classe correcta da Morada2
    # rua: str
    # num: str
    # apt: str
    # cp: int
    #propriedades acima ficam redundantes com constructor criado

    def __init__(self, rua: str, num: str, apt: str, cp: int):
        self.rua = rua
        self.num = num
        self.apt = apt
        self.cp = cp
