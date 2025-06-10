class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev 
        self.autok = []
        self.berlesek= []
        
    def autok_hozzaadasa(self,auto):
        self.autok.append(auto)
    
    def berel(self, rendszam,datum ,ugyfelneve):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "Nincs ilyen autó"
    
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                return "Az autó már foglalt ezen a napon"
            
        berles = berles(auto, datum,ugyfelneve)
        self.berlesek.append(berles)
        return f"Bérlés sikeres, ára : {auto.berletidij} Ft"
    
    def lemondas(self,rendszam,datum,ugyfelneve):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum and b.ugyfelneve == ugyfelneve:
                self.berlesek.remove(b)
                return "A bérlés lemondva"
            return "Nem található ilyen bérlés"
        
    def listazberlesek(self):
        if not self.berlesek:
            return "Nincs aktív bérlés"
        return "\n".join(b.info() for b in self.berlesek)
        