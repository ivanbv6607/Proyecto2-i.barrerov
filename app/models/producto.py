#from models.iProducto import IProducto
#from models.ingrediente import Ingredientes
from config.db import db
from models.ingrediente_producto import producto_ingrediente
from sqlalchemy import ForeignKey

"""producto_ingrediente = db.table('producto_ingrediente',
    db.column('producto_id', db.Integer, db.ForeignKey('producto.id'), primary_key=True),
    db.column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
)"""

""" Se importa la clase padre iProducto"""
class Productos(db.Model):
        __tablename__ = 'productos'

        id = db.Column(db.Integer, primary_key=True)
        nombre = db.Column(db.String(200))
        precio = db.Column(db.Float, nullable=False)
        tipo = db.Column(db.Boolean, nullable=True)
        ing1 = db.Column(db.Integer, nullable=False)
        ing2 = db.Column(db.Integer, nullable=False)
        ing3 = db.Column(db.Integer, nullable=False)

        def obtener_nombre(self):
            return self._nombre
    
        def actualizar_nombre(self, nombre):
            self._nombre = nombre

        def obtener_precio(self):
            return self._precio
    
        def actualizar_precio(self, precio):
            self._nombre = precio

        def calcular_rentabilidad(self):
            return self.precio - self.calcular_costo_producto()
    
        def calcular_costo_producto(self):
            return sum(ingrediente.precio for ingrediente in self.ingredientes)
    
        def calcular_calorias(self):
            return sum(ingrediente.calorias for ingrediente in self.ingredientes)
    
p1 = {'nombre' : 'Samurai de fresas', 'rentabilidad': 4900}
p2 = {'nombre': 'Samurai de mandarinas', 'rentabilidad': 2500}
p3 = {'nombre': 'Malteda chocoespacial', 'rentabilidad': 11000}
p4 = {'nombre': 'Cupihelado', 'rentabilidad': 3200}
