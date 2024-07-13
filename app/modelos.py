from enum import Enum , auto

class TipoEntrada(Enum):
    Bebe = auto()
    Niño = auto()
    Adulto = auto()
    Jubilado = auto()

class Entrada:
    def __init__(self, edad: int):
        
        if edad >99:
            raise ValueError("Debe escribir una edad menor de 100")

        if edad <0:
            raise ValueError("No debe escribir una edad negativa")
        elif edad <= 2:
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

class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.numero_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.Bebe : {'Q':0,'P':0},
            TipoEntrada.Niño :  {'Q':0,'P':14},
            TipoEntrada.Adulto :  {'Q':0,'P':23},
            TipoEntrada.Jubilado : {'Q':0,'P':18}
        }
     

    def add_entrada(self, edad):
        """
         En función de la edad,crear una entrada y incrementar el contador de entradas
         Con el precio de la entrada nueva incrementar el total
        """

        nueva_entrada = Entrada(edad)
        self.numero_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo]['Q'] += 1
     
    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada):   
        return self.tipos_entrada[tipo]['Q']

    def subtotal_tipo(self, tipo: TipoEntrada)->int:
        return  self.tipos_entrada[tipo]['Q'] * self.tipos_entrada[tipo]['P']      