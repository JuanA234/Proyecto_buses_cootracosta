import numpy as np

class Bus:

    def __init__(self, numeroIdentificacion, placa, conductor):

        self.numeroIdentificacion = numeroIdentificacion
        self.placa = placa
        self.conductor = conductor
        self.sillas = np.full((4,10),1)
        letrasAlfabeto = ("A","B","C","D","E","F","G","H","I","J")
        self.Estado = (1,2,3)


    def ModificarIdentificacion(self, numeroDeIdentificacion):
        self.numeroIdentificacion = numeroDeIdentificacion

    def ModificarPlaca(self, placa):
        self.placa = placa

    def ModificarConductor(self, conductor):
        if len(conductor) != 0:
            self.conductor = conductor

    def ModificarEstadoAsiento(self, fila, columna, Estado):
        self.sillas[fila][columna] = Estado
        