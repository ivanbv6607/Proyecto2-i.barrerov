from app.config.db import db
from app.models.ingrediente import Ingredientes


producto_ingrediente = db.table('producto_ingrediente',
    db.Column('producto_id', db.Integer, db.ForeignKey('productos.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)
)

class Productos(db.Model):
        __tablename__ = 'productos'

        id = db.Column(db.Integer, primary_key=True)
        nombre = db.Column(db.String(200))
        precio = db.Column(db.Float, nullable=False)
        tipo = db.Column(db.Boolean, nullable=True) # Es copa o malteada
        ing1 = db.Column(db.Integer, nullable=False)
        ing2 = db.Column(db.Integer, nullable=False)
        ing3 = db.Column(db.Integer, nullable=False)

        """ingrediente = db.relationship(
                                'Ingredientes', 
                                secondary='producto_ingrediente',
                                primaryjoin='productos.id == producto_ingrediente.c.producto_id',
                                secondaryjoin='producto_ingrediente.c.ingrediente_id == ingredientes.id',
                                            back_populates='productos',)"""


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
            return sum(ingrediente.costo for ingrediente in self.ingredientes)
    
        def calcular_calorias(self):
            caloria_1 = Ingredientes.obtener_calorias(self.ing1)
            caloria_2 = Ingredientes.obtener_calorias(self.ing2)
            caloria_3 = Ingredientes.obtener_calorias(self.ing3)
            return (caloria_1+caloria_2+caloria_3)
            #return sum(ingrediente.calorias for ingrediente in self.ingredientes)
    
p1 = {'nombre' : 'Samurai de fresas', 'rentabilidad': 4900}
p2 = {'nombre': 'Samurai de mandarinas', 'rentabilidad': 2500}
p3 = {'nombre': 'Malteda chocoespacial', 'rentabilidad': 11000}
p4 = {'nombre': 'Cupihelado', 'rentabilidad': 3200}
