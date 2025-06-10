from auto import Auto

class Szemelyauto(Auto):
    def __init__(self,rendszam,tipus, berletidij,utasszam):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berletidij = berletidij
        self.utasszam = utasszam
    
    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérletidíj: {self.berletidij}  Ft/nap, Utasok: {self.utasszam} "
        

