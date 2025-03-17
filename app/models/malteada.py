from producto import Producto
from ingrediente import Ingrediente
from base import Base
from complemento import Complemento

class Malteada(Producto):

    """
    Malteada que hereda de la Clase Producto
        def __init__(self, nombre:str, precio:float, ing1:Ingrediente, ing2:Ingrediente, ing3:Ingrediente, volumen:int):
        super().__init__(nombre, precio, ing1, ing2, ing3)
        def calcular_costo_producto(self):


    """

    def __init__(self, nombre:str, precio:float, ing1:Ingrediente, ing2:Ingrediente, ing3:Ingrediente, volumen:int):
        super().__init__(nombre, precio, ing1, ing2, ing3)
        self._volumen = volumen

    def calcular_costo_producto(self):
        costo1 = self.ing1.obtener_costo()
        costo2 = self.ing2.obtener_costo()
        costo3 = self.ing3.obtener_costo()
        return costo1 + costo2 + costo3
    
    def calcular_calorias(self):
        calorias1 = self.ing1.obtener_calorias()
        calorias2 = self.ing2.obtener_calorias()
        calorias3 = self.ing3.obtener_calorias()
        return round(calorias1 + calorias2 + calorias3 + 200)   # Se le adiciona 200 calorias por la crema chantilli

