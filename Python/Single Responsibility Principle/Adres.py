class Adres:
    def __init__(self):
        self.ulke = None
        self.il = None
        self.ilce = None
        self.postkodu = None

    def getulke(self):
        return self.ulke

    def setulke(self, ulke):
        self.ulke = ulke

    def getil(self):
        return self.il

    def setil(self, il):
        self.il = il

    def getilce(self):
        return self.ilce

    def setilce(self, ilce):
        self.ilce = ilce

    def getpostkodu(self):
        return self.postkodu

    def setpostkodu(self, postkodu):
        self.postkodu = postkodu
        
    def __str__(self):
        return f"{self.ulke} {self.il} {self.ilce} {self.postkodu}"

