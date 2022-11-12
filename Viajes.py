from Bus import *

class Viaje:
    def _init__ (self, bus:Bus):
        self.bus = bus
        self.conductor = self.bus.conductor
        
