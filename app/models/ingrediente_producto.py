from config.db import db
#from models.producto import Productos
#from models.ingrediente import Ingredientes
from sqlalchemy import ForeignKey

producto_ingrediente = db.Table("producto_ingrediente",
        db.Column("producto",db.Integer, ForeignKey('Productos.id'), primary_key=True),
        db.Column("ingrediente",db.Integer, ForeignKey('Ingredientes.id'), primary_key=True))                         
                                                  
"""class Producto_ingrediente(db.Model):
id = db.Column(db.Integer, primary_key=True) 
producto = db.column(db.Integer, db.ForeignKey('Productos.id'))
ingrediente = db.column(db.Integer, db.ForeignKey('Ingredientes.id')) """                        
                         