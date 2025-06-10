class Berles:
    def __init__(self,auto, datum,ugyfelneve):
        self.auto = auto
        self.datum = datum
        self.ugyfelneve = ugyfelneve
    
    def info(self):
        return f"{self.ugyfelneve} bérelte: {self.auto.rendszam}, ekkor: {self.datum}"