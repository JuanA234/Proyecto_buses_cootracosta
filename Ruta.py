import numpy as np
class Ruta:
    def __init__(self, ciudadOrigen:str, ciudadDestino:str, horaSalida:int, costoPasaje:float, busEnRuta):
        self.ciudadOrigen= ciudadOrigen
        self.ciudadDestino= ciudadDestino
        self.horaSalida= horaSalida
        self.costoPasaje= costoPasaje
        self.busEnRuta= busEnRuta
        self.ciudadesOpciones=("Santa Marta", "Barranquilla", "Cartagena", "Valledupar", "Monteria", "Sincelejo", "Riohacha")

    def ConfigurarCiudadOrigen(self, ciudadOrigen:str):
        if ciudadOrigen in self.ciudadesOpciones:
            self.ciudadOrigen= ciudadOrigen
    
    def ConfigurarCiudadDestino(self, ciudadDestino:str):
        ciudadOrigen= self.ciudadOrigen
        if ciudadDestino in self.ciudadesOpciones:
            if ciudadDestino!=ciudadOrigen:
                self.ciudadDestino=ciudadDestino

    def ConfigurarHoraSalida(self, horaSalida:float):
        if 0<=horaSalida<=23:
            self.horaSalida= horaSalida
    
    def ConfigurarCostoPasaje(self):
        horaSalida= self.horaSalida
        tarifaBase=10000
        costoFinal=0
        if 0<=horaSalida<=6:
            costoFinal= tarifaBase
        elif 7<=horaSalida<=12:
            costoFinal= tarifaBase*2
        elif 1<=horaSalida<=2:
            costoFinal=tarifaBase*5
        elif 3<=horaSalida<=7:
            costoFinal=tarifaBase*4
        else:
            costoFinal=tarifaBase*3.5
        self.costoPasaje= costoFinal

