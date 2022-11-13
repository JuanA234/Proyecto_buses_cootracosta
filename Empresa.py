
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


    def AgregarRuta(self, ruta:Ruta): 
        rutaAgregada= False
        posibilidadAgregarRuta= False
        rutas: Ruta
        for rutas in self.listaRutas:
            if (ruta[0]==self.listaRutas[rutas[0]]) and (ruta[1]==self.listaRutas[rutas[1]]) and (ruta[2]==self.listaRutas[rutas[2]]):
                posibilidadAgregarRuta=False
            else:
                posibilidadAgregarRuta=True
        if posibilidadAgregarRuta==True:
            self.listaRutas.append(ruta)
            rutaAgregada= True
        return rutaAgregada


