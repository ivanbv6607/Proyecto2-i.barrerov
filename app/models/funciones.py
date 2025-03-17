def es_sano(self,calorias:int, vegetariano:bool):
    if self.calorias < 100 or self.vegetariano:
        return True
    return False

def calcular_calorias(calorias_ing1:int ,calorias_ing2:int, calorias_ing3:int):
    return round(calorias_ing1+calorias_ing2+calorias_ing3)*.95,2

def calcular_costo_producto(ingrediente1:dict, ingrediente2:dict, ingrediente3:dict):
    costo = 0
    lista = [ingrediente1, ingrediente2, ingrediente3]
    for ingrediente in lista:
        costo += ingrediente['costo']
    return costo

def calcular_rentabilidad(precio_vta:float ,ingrediente1:dict, ingrediente2:dict, ingrediente3:dict):
    costo = calcular_costo_producto(ingrediente1, ingrediente2, ingrediente3)
    return precio_vta - costo
    
def producto_mas_rentable(producto_1:dict,producto_2:dict,producto_3:dict,producto_4:dict):
    mas_rentable = 0
    lista = [producto_1, producto_2, producto_3, producto_4]
    for producto in lista:
        if mas_rentable < producto['rentabilidad']:
            mas_rentable = producto['rentabilidad']
    return mas_rentable

p1 = {'nombre' : 'Samurai de fresas', 'rentabilidad': 4900}
p2 = {'nombre': 'Samurai de mandarinas', 'rentabilidad': 2500}
p3 = {'nombre': 'Malteda chocoespacial', 'rentabilidad': 11000}
p4 = {'nombre': 'Cupihelado', 'rentabilidad': 3200}

ig1 = {'nombre': 'Helado de Fresa', 'costo': 1200}
ig2 = {'nombre': 'Chispas de chocolate', 'costo': 500}
ig3 = {'nombre': 'Mani Japonés', 'costo': 900}

print(producto_mas_rentable(p1,p2,p3,p4))

print(f" Costo del producto {calcular_costo_producto(ig1,ig2,ig3)}")

print(f" Rentabilidad {calcular_rentabilidad(7500,ig1,ig2,ig3)}")

