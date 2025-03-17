from abc import ABC,abstractmethod
from models.ingrediente import Ingredientes

class IProducto(ABC):

    """ La clase abstracta que tiene los métodos
    def calcular_costo_producto(self):
    def calcular_rentabilidad(self):
    def calcular_calorias(ingrediente1:str, ingrediente2:str, ingrediente3:str):
   
    """
    @abstractmethod
    def calcular_costo_producto(self):
        pass
    
    @abstractmethod
    def calcular_rentabilidad(self):
        pass
    
    @abstractmethod
    def calcular_calorias(ingrediente1:Ingredientes, ingrediente2:Ingredientes, ingrediente3:Ingredientes):
        pass
