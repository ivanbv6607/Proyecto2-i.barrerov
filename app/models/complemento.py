from ingrediente import Ingrediente

class Complemento(Ingrediente):
    """
        Esta clase tiene el ingrediente que es complemento de los productos de la heladeria:
        
        def __init__(self,nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str):
        super().__init__(nombre, costo, calorias, inventario, es_vegetariano, tipo)

        def abastecer(self):
        def renovar_inventario(self):
    """
    def __init__(self,nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str):
        super().__init__(nombre, costo, calorias, inventario, es_vegetariano, tipo)

        self.tipo = "C"
 
    def abastecer(self):
        self.inventario +=10

    def dar_de_baja_inventario(self):
        self.inventario = 0

    def abastecer(self):
        self.inventario +=1
    