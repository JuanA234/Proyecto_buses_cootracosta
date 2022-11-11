from datetime import date

class Cliente:

    def __init__(self, nombre, identificacion, añoDeNacimiento, mesDeNacimiento, diaDeNacimiento):

        self.nombre = nombre
        self.identificacion = identificacion
        self.añoDeNacimiento = añoDeNacimiento
        self.mesDeNacimiento = mesDeNacimiento
        self.diaDeNacimiento = diaDeNacimiento

        def CalcularEdad(self):
            fechaDeHoy = date.today()
            edad = None
            restar = 0
            diferenciaDeAños = fechaDeHoy.year - self.añoDeNacimiento
            diferenciaDeMeses = fechaDeHoy.month - self.mesDeNacimiento
            diferenciaDeDias= fechaDeHoy.day - self.diaDeNacimiento
            if diferenciaDeMeses < 0 or (diferenciaDeMeses == 0 and diferenciaDeDias < 0):
                restar = 1
            edad = diferenciaDeAños - restar
            return edad

