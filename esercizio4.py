# esercizio dalla scheda: calcolare a scelta area di un quadrato, rettangolo, triangolo e cerchio
Forma = input("Scrivi il poligono (in minuscolo) di cui desideri calcolare l'area: ")
if Forma == "cerchio":
    raggio = int(input("Inserisci il raggio: "))
    Area = raggio**2* 3.14 
    print("Area è uguale a ", Area)
elif Forma == "quadrato":
    lato = int(input("Inserisci lato: "))
    Area = lato**2 
    print ("Area è uguale a ", Area)
elif Forma == "rettangolo":
    base = int(input("Inserisci base: "))
    altezza = int(input("Inserisci altezza: "))
    Area = base*altezza
    print ("Area è uguale a ", Area)
elif Forma == "triangolo":
    base = int(input("Inserisci base: "))
    altezza = int(input("Inserisci altezza: "))
    Area = base*altezza/2
    print ("Area è uguale a ", Area)
else:
    print("Poligono non valido...")