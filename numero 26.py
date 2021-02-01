'''
esercizio pagina 73 numero 26:calcola la media degli stipendi dei dipendenti di un'azienda, acquista con 
una ripetizione fino a quandosi inserisce il valore -1 per segnalare la fine dell'input dei dati
'''
somma = 0
conto = 0
while True:
    stipendio = int(input("scrivi stipendio: "))
    if stipendio == -1: 
        break
    else :
        somma += stipendio
        conto+= 1
        media = somma/conto
print("la media è: %s" % media)

