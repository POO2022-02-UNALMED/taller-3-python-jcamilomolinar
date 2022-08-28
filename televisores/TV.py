class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        self.aumentoNumtv()

    @classmethod
    def aumentoNumtv(cls): cls._numTV += 1

    def setMarca(self, Nmarca): self._marca = Nmarca
    
    def getMarca(self): return self._marca

    def setControl(self, Ncontrol): self._control = Ncontrol
    
    def getControl(self): return self._control

    def setPrecio(self, Nprecio): self._precio = Nprecio

    def getPrecio(self): return self._precio

    def setVolumen(self, Nvolumen):
        if 0 <= Nvolumen <= 7 and self._estado: self._volumen = Nvolumen
    
    def getVolumen(self): return self._volumen

    def setCanal(self, Ncanal):
        if 1 <= Ncanal <= 120 and self._estado: self._canal
    
    def getCanal(self): return self._canal

    @classmethod
    def setNumTV(cls,N): cls._numTV = N

    @classmethod
    def getNumTV(cls): return cls._numTV

    def turnOn(self): self._estado = True

    def turnOff(self): self._estado = False

    def getEstado(self): return self._estado

    def canalUp(self):
        if self._canal <= 119 and self._estado: self._canal += 1
    
    def canalDown(self):
        if self._canal >= 2 and self._estado: self._canal -= 1

    def volumenUp(self):
        if self._canal <= 6 and self._estado: self._volumen += 1
    
    def volumenDown(self):
        if self._canal >= 1 and self._estado: self._volumen -= 1