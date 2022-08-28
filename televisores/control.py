class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self): self._tv.turnOn()

    def turnOff(self): self._tv.turnOff()

    def canalUp(self): self._tv.canalUp()
    
    def canalDown(self): self._tv.canalDown()

    def volumenUp(self): self._tv.volumenUp()
    
    def volumenDown(self): self._tv.volumenDown()

    def setCanal(self, Ncanal): self._tv.setCanal(Ncanal)

    def enlazar(self, Ntv):
        self._tv = Ntv
        Ntv.setControl(self)

    def getTv(self): return self._tv

    def setTv(self, Ntv): self._tv = Ntv