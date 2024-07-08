from enum import Enum , auto

class TipoEntrada(Enum):
    Bebe = auto()
    Niño = auto()
    Adulto = auto()
    Jubilado = auto()

class Entrada:
    def __init__(self, edad: int):
        if edad <= 2:
            self.tipo = TipoEntrada.Bebe
            self.precio = 0
        elif edad <13:
            self.tipo = TipoEntrada.Niño
            self.precio = 14
        elif edad <65:
            self.tipo = TipoEntrada.Adulto
            self.precio = 23
        else:
            self.tipo = TipoEntrada.Jubilado
            self.precio = 18            
            