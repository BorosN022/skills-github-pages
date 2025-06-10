from szemelyauto import Szemelyauto
from teherauto import Teherauto
from autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Kiadás")
    
    #autók
    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5)
    auto2 = Szemelyauto("LLS-445", "Tesla", 20000, 4)
    auto3 = Szemelyauto("KBM-221", "Jeep", 30000, 1000)
    
    kolcsonzo.autok_hozzaadasa(auto1)
    kolcsonzo.autok_hozzaadasa(auto2)
    kolcsonzo.autok_hozzaadasa(auto3)
    
    #Bérlések
    
    kolcsonzo.berel("ABC-123", "2025-03-02", "Kiss Jani")
    kolcsonzo.berel("LLS-445", "2025-04-06", "Kiss Janna")
    kolcsonzo.berel("KBM-221", "2025-05-05", "Jadló")
    kolcsonzo.berel("ABC-123", "2025-06-03", "Kovács Gergő")
    
    
    while True:
        print("\n1. Autó bérlése\n2. Bérlés lemondása\n3. Bérlések listázása\n4. Kilépés")
        valasztas = input("Választás: ")
        
        if valasztas == "1":
            rendszam = input("rendszám: ")
            datum = input("dátum: ")
            nev = input("név: ")
            print(kolcsonzo.berel(rendszam, datum, nev)) 
        elif valasztas =="2":
             rendszam = input("rendszám: ")
             datum = input("dátum: ")
             nev = input("név: ")
             print(kolcsonzo.lemondas(rendszam,datum,nev))
        elif valasztas == "3":
            print(kolcsonzo.listazberlesek())
        elif valasztas == "4":
            print("Kilépés")
            break
        else: 
            print("Érvénytelen a választás")
    
    if __name__ == "__main__":
        main()
    
    
    
    
    
    
