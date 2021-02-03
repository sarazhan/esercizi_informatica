'''
Consegna 04/01/21: Dall'es. 16 pagina 189, costruisci un dizionario che ha come chiave la capitale e valore la nazione. 
E usa il nuovo dizionario per trovare il nome della nazione, noto la capitale.
'''
def geografia():
    diz = {}
    controllo = int(input("Quante capitali vuoi inserire? "))
    for n in range(controllo):
        capitale = input("Inserisci la capitale: ")
        nazione = input("Inserisci la nazione della capitale: ")
        diz[capitale] = nazione

    domanda = input("Inserisci una capitale per sapere la sua nazione: ")
    if domanda not in diz:
        print("Errore: non hai inserito questa capitale nel dizionario.")
    else:
        risposta = diz[domanda]
        print(risposta)

geografia()
