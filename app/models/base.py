from ingrediente import Ingrediente

class Base(Ingrediente):
    """
        Esta clase tiene el ingrediente que es base de los productos de la heladeria:
        
        def __init__(self,nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str, sabor:str):
        super().__init__(nombre, costo, calorias, inventario, es_vegetariano, tipo)
        def actualizar_sabor(self, sabor):
        def obtener_sabor(self):
        def abastecer(self):
    """

    def __init__(self,nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str, sabor:str):
        super().__init__(nombre, costo, calorias, inventario, es_vegetariano, tipo)
        self.sabor = sabor
        self.tipo = "B"
    
    def actualizar_sabor(self, sabor):
         self.sabor = sabor

    def obtener_sabor(self):
         return self.sabor
    
    def abastecer(self):
        self.inventario +=5