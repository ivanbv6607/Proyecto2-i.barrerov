import unittest

from models.ingrediente import Ingredientes
from models.base import Base
from models.copa import Copa
from models.malteada import Malteada
from models.complemento import Complemento
from models.producto import Productos
from controllers.home_controller import vender


class Test_ingredientes(unittest.TestCase):
    def test_es_sano(self):
        ingrediente = Ingredientes(id = 1, nombre = " Helado de fresa", costo = 500.0, calorias = 150, inventario=2, es_vegetariano=False)
        self.assertEqual(ingrediente.es_sano(), False)

    def test_abastecer_base(self):
        base = Base(id = 8, nombre = "Mandarinas", costo = 150.0, calorias = 300, inventario=9, es_vegetariano=True)
        self.assertEqual(base.abastecer(), 7)

    def test_abastecer_complemento(self):
        complemento = Complemento(id = 1, nombre = " Helado de fresa", costo = 500.0, calorias = 150, inventario=2, es_vegetariano=False)
        self.assertEqual(complemento.abastecer(), 3)
   

    def test_calcular_calorias_copa(self):
        copa = Copa(nombre="Cupihelado", precio = 2000, ing1 = 2, ing2 = 5, ing3 = 6)
        self.assertEqual(copa.calcular_calorias(), 7)

    def test_calcular_calorias_malteada(self):
        malteada = Malteada(nombre="Malteada chocoespacial", precio = 3500, ing1 = 6, ing2 = 3, ing3 = 9)
        self.assertEqual(malteada.calcular_calorias(), 7)

    def test_costo_producto_malteada(self):
        malteada = Malteada(nombre="Malteada chocoespacial", precio = 3500, ing1 = 6, ing2 = 3, ing3 = 9)
        self.assertEqual(malteada.calcular_costo_producto(), 7)

    def test_costo_producto_copa(self):
        copa = Copa(nombre="Samurai de fresas", precio = 1200, ing1 = 1, ing2 = 4, ing3 = 7)
        self.assertEqual(copa.calcular_costo_producto(), 7)

    def test_calcular_rentabilidad(self):
        producto = Productos(nombre="Samurai de fresas", precio = 1200, ing1 = 1, ing2 = 4, ing3 = 7)
        self.assertEqual(producto.calcular_rentabilidad(), 7)

    def test_mas_rentable(self):
        producto1 = Productos(nombre="Samurai de fresas", precio = 1200, ing1 = 1, ing2 = 4, ing3 = 7)
        producto2 = Productos(nombre="Malteada chocoespacial", precio = 3500, ing1 = 6, ing2 = 3, ing3 = 9)
        producto3 = Productos(nombre="Cupihelado", precio = 2000, ing1 = 2, ing2 = 5, ing3 = 6)
        producto4 = Productos(nombre="Samurai de Mandarinas", precio = 2000, ing1 = 8, ing2 = 3, ing3 = 7)
        self.assertEqual(producto.calcular_rentabilidad(), 7)

    def test_vender(self):
        producto = Productos(nombre="Samurai de fresas", precio = 1200, ing1 = 1, ing2 = 4, ing3 = 7)
        self.assertEqual(producto.vender(), "Vendido!")

  