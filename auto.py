from abc import ABC , abstrackmethod

class Auto(ABC):
    def __init__(self, rendszam: str , tipus: str, berletidij: int):
        self.rendszam = rendszam
        self.tipus = tipus 
        self.berletidij = berletidij
        
@abstrackmethod
def info(self):
    pass