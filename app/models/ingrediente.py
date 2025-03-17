from config.db import db
from models.ingrediente_producto import producto_ingrediente
from sqlalchemy import ForeignKey

class Ingredientes(db.Model):
    """ Define el ingrediente de los productos
        def __init__(self, nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str):
        def es_sano(self,calorias:int, vegetariano:bool):
        def obtener_nombre(self):
        def actualizar_nombre(self, nombre):
        def obtener_costo(self):
        def actualizar_costo(self, costo):
        def obtener_calorias(self):
        def actualizar_calorias(self, calorias):
        def obtener_inventario(self):
        def actualizar_inventario(self, inventario):
        def obtener_vegetariano(self):
        def actualizar_es_sano(self, es_sano):
        """
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    costo = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Boolean, nullable=True)    
    es_vegetariano = db.Column(db.Boolean, nullable=True)

    def __init__(self, nombre:str, costo:float, calorias:int, inventario:float, es_vegetariano:bool, tipo:str):
        self._nombre = nombre
        self._costo = costo
        self._calorias = calorias
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano
        self.tipo = None
    
    def es_sano(self,calorias:int, vegetariano:bool):
        if self._calorias < 100 or self.es_vegetariano:
            return True
        return False
    
    def abastecer():
        pass

    def obtener_nombre(self):
        return self._nombre
    
    def actualizar_nombre(self, nombre):
        self._nombre = nombre
    
    def obtener_costo(self):
        return self._costo
    
    def actualizar_costo(self, costo):
        self._costo = costo
  
    def obtener_calorias(self):
        return self._calorias
    
    def actualizar_calorias(self, calorias):
        self._calorias = calorias
  
    def obtener_inventario(self):
        return self.inventario

    def actualizar_inventario(self, inventario):
        self.inventario = inventario    
    
    def obtener_es_vegetariano(self):
        return self.es_vegetariano
    
    def actualizar_es_sano(self, es_sano):
        self.es_sano = es_sano  

    def es_sano(self,calorias:int, vegetariano:bool):
        if self.calorias < 100 or self.vegetariano:
            return True
        return False
    
    def abastecer(self):
        self.inventario +=5