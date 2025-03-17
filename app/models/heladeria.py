from producto import Producto

from config.db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable= True)
    description = db.Column(db.Text, nullable= True)
    done = db.Column(db.Boolean, default=False, nullable=True)

class Heladeria():
    """ 
    Clase Heladeria:
    def __init__(self, producto1:Producto, producto2:Producto, producto3:Producto, producto4:Producto, telefono:str, 
             email:str, ventas_dia:float):
    funciones: 
    def obtener_telefono(self):
    def actualizar_telefono(self,telefono):
    def obtener_email(self):
    def actualizar_email(self,email):
    def obtener_ventas_dia(self):
    def actualizar_ventas_dia(self,ventas_dia):
    def producto_mas_rentable(self)->dict:
        
    """
    def __init__(self, producto1:Producto, producto2:Producto, producto3:Producto, producto4:Producto, telefono:str, email:str, ventas_dia:float):
        self.producto1 = producto1
        self.producto2 = producto2
        self.producto3 = producto3
        self.producto4 = producto4
        self._telefono = telefono
        self._email = email
        self._ventas_dia = ventas_dia

    def obtener_telefono(self):
        return self._telefono
    
    def actualizar_telefono(self,telefono):
        self._telefono = telefono

    def obtener_email(self):
        return self._email

    def actualizar_email(self,email):
        self._email = email    

    def obtener_ventas_dia(self):
        return self._ventas_dia
    
    def actualizar_ventas_dia(self,ventas_dia):
        self._ventas_dia = ventas_dia
    
    def producto_mas_rentable(self)->dict:
        mas_rentable = 0.0

        rent1 = self.producto1.calcular_rentabilidad()
        mas_rentable = rent1
        nombre = self.producto1._nombre

        rent2 = self.producto2.calcular_rentabilidad()
        if mas_rentable < rent2:
            mas_rentable = rent2 
            nombre = self.producto2._nombre 

        rent3 = self.producto3.calcular_rentabilidad()
        if mas_rentable < rent3:
            mas_rentable = rent3
            nombre = self.producto3._nombre

        rent4 = self.producto4.calcular_rentabilidad()
        if mas_rentable < rent4:
            mas_rentable = rent4
            nombre = self.producto4._nombre
        return {"nombre":nombre,"rentabilidad":mas_rentable}
    
