'''
esercizio numero pag.73 numero 28: un elenco di studenti partecipanti a una gara sportiva di lancio del peso 
(nome studente, lancio), visualizza il valore del lancio del vincitore(valore massimo)
'''
lista_nomi = input("Nomi di ogni partencipante poi stccato da uno spazio l'altro partecipante:  ").split()
lista_punteggio = []
lunghezza = int(len(lista_nomi))
for i in range(lunghezza):
    punteggio = int(input("Scrivi il punteggio del partecipante corrispondente e invia: "))
    lista_punteggio.append(punteggio)
puntomax = max(lista_punteggio)
posizione = int(lista_punteggio.index(puntomax))
vincitore = lista_nomi[posizione]
print(" Vincitore è : ", vincitore, puntomax)
