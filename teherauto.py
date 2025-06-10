from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berletidij, teherbiras):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berletidij = berletidij
        self.teherbiras = teherbiras
        
    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérletidíj: {self.berletidij}  Ft/nap, Teherbírás: {self.teherbiras} kg."