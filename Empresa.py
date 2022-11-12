
from typing import List
from Bus import Bus
from Rutas import Rutas
class Empresa:

    
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.buses : List[Bus] = []
        self.rutas : List[Rutas]
        #self.ciudadesOperacion = ("Santa Marta", "Barranquilla", "Valledupar", "Monteria", "Riohacha", "Sincelejo", "Cartagena")
        #self.tamañosDeBus = (7, 11, 13)
        
    def AgregarBus(self, bus:Bus):
        busAgregado = False
        self.buses.append(bus)
        busAgregado = True
        return busAgregado


    def AgregarRutas(self): 
        pass


