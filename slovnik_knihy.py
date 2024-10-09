# funkce pridat_knihu
def pridat_knihu(knihy):
    nazev = input("Zadej název knihy: ")
    if nazev in knihy:
        print(f"Kniha s názvem {nazev} v knihovně už je. ")
        return
    
    autor = input(f"Zadej autora knihy {nazev}: ")

    while True:
        try:
            rok = int(input(f"Zadej rok vydání knihy {nazev}: "))
            break
        except ValueError:
            print("Zadej prosím celé číslo. Zkus knihu zadat znovu")

    knihy[nazev] = {"autor": autor, "rok": rok}
    print(f"Kniha {nazev} byla přidána.")


# funkce odebrat_knihu
def odebrat_knihu(knihy):
    nazev = input("Zadej název knihy k odebrání: ")
    if nazev in knihy:
        del knihy[nazev]
        print(f"Kniha s názvem {nazev} byla odebrána.")
    else:
        print(f"Kniha s názvem {nazev} není v knihovně.")

# funkce vyhledat_knihu
def vyhledat_knihu(knihy):
    nazev = input("Zadej název knihy kterou chces vyhledat: ")
    if nazev in knihy:
            print(f"Nazev: {nazev}\nAutor: {knihy[nazev]['autor']}\nRok vydání: {knihy[nazev]['rok']} ")
    else:
            print(f"Kniha s názvem {nazev} není v knihovně.")


# hlavní program
knihy = {}

def hlavni_program():
   
    while True:
        print("\nVyber možnost 1 pro přidání knihy.")
        print("Vyber možnost 2 pro odebrání knihy.")
        print("Vyber možnost 3 pro vyhledání knihy.")
        print("Vyber možnost 4 pro ukončení programu.")
        try:
            vyber = int(input("\nVyber možnost: "))
            if vyber == 1:
                pridat_knihu(knihy)
            elif vyber == 2:
                odebrat_knihu(knihy)
            elif vyber == 3:
                vyhledat_knihu(knihy)
            elif vyber == 4:
                print("Program byl ukončen.")
                exit()
            else:
                print("Zadej prosím správné číslo.")
        except ValueError:
            print("Zadej prosím celé číslo.")
        
    
hlavni_program()