from models.iProducto import iProducto
from ingrediente import Ingrediente
from base import Base
from complemento import Complemento
from config.db import db

class Copa(iProducto):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    precio = db.Column(db.Float, nullable=False)
    id_ing1 = db.Column(db.Integer, nullable=False)
    id_ing2 = db.Column(db.Integer, nullable=False)
    id_ing3 = db.Column(db.Integer, nullable=False)

    """Clase hereda de la clase producto
    def __init__(self, nombre:str, precio:float, ing1:Ingrediente, ing2:Ingrediente, ing3:Ingrediente, tipo_vaso:str):
    super().__init__(nombre, precio, ing1, ing2, ing3)
    def calcular_calorias(ing1:str, ing2:str, ing3:str):
    """

    def __init__(self, nombre:str, precio:float, ing1:Ingrediente, ing2:Ingrediente, ing3:Ingrediente, tipo_vaso:str):
        super().__init__(nombre, precio, ing1, ing2, ing3)
        self._tipo_vaso = tipo_vaso

    def calcular_costo_producto(self):
        costo1 = self.ing1.obtener_costo()
        costo2 = self.ing2.obtener_costo()
        costo3 = self.ing3.obtener_costo()
        return costo1 + costo2 + costo3 + 500   # Se le adiciona $500 por el vaso de la copa
    
    def calcular_calorias(self):
        calorias1 = self.ing1.obtener_calorias()
        calorias2 = self.ing2.obtener_calorias()
        calorias3 = self.ing3.obtener_calorias()
        return round(((calorias1+calorias2+calorias3)*.95))
    
    
        