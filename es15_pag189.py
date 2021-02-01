# Consegna 28/01/21: Dato un elenco di nazioni e uno di capitali, visualizza la capitale di una nazione fornita dalla tastiera o un messaggio di errore.
def geografia():
    nazione = input("Inserisci nazioni in ordine, separati da uno spazio: ").split()
    capitali = input("Inserisci capitali in ordine, separali con uno spazio: ").split()
    domanda = input("Inserisci la nazione di cui vuoi sapere la rispettiva capitale: ")
    indice = nazione.index(domanda)
    if domanda not in nazione:
        print("Errore: la nazione inserita non è presente nella lista inserita.")
    else:
        print("La sua capitale è:", capitali[indice])
        
geografia()