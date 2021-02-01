'''
Consegna 28/01/21: riferimento a es 15 pag 189, crea dizionario chiave = nazione e valore = capitale. 
Poi visualizza la capitale di una nazione fornita dalla tastiera o un messaggio di errore.
'''

def geografia():
    diz = {}
    controllo = int(input("Quante nazioni vuoi inserire? "))
    for n in range(controllo):
        nazione = input("Inserisci la nazione: ")
        capitale = input("Inserisci la capitale della nazione: ")
        diz[nazione] = capitale

    domanda = input("Inserisci una nazione per sapere la sua nazione: ")
    if domanda not in diz:
        print("Errore: non hai inserito questa capitale nel dizionario.")
    else:
        risposta = diz[domanda]
        print(risposta)
        
geografia()