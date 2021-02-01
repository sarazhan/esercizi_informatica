'''
esercizio a pag.73 numero 30:fornisci la rappresentazione decimale di un numero binario, all'inizio si richiede il numero di cifre 
di cui è composto il numero binario lunghezza si esegue pure una ripetizione che richiede le cifre della potenza di 2 corrispondente
alla posizione della cifra binaria aggiunge il risultato dalla somma la ripetizione viene eseguita per il contatore che va dal valore 0 
al valore di lunghezza diminuito di 1. Confronta poi il risultato con il valore ottenuto dalla funzione predefinita 
del linguaggio per convertire un numero binario in decimale
'''
lunghezza = int(input("Quanto è lungo il tuo numero binario? "))
binario = ""
decimale = 0
for n in range(lunghezza):
    print ("La", n+1, "° partendo da destra ")
    cifra = input()
    binario = cifra + binario
    cifra = int(cifra)
    decimale = decimale + (cifra*(2**n))
binario = int(binario, 2)
print ("Confronto dei risultati:", binario,"e", decimale)
