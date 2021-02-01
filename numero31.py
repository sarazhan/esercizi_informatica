'''
esercizio pagina 73 numero 31: Fornisce la rappresentazione in binario di un numero decimale dopo aver acquisito
il valore del numero da trasformare segue la divisione del numero per due e si calcola quoziente e resto. Il resto è 
la prima cifra della rappresentazione binaria. Si ripete il procedimento assegnando il quoziente ottenuto a Numero e 
ricalcolando la divisione per 2; la ripetizione prosegue finché il quoziente ottenuto è uguale a zero. La rappresentazione 
binaria del numero decimale è costituita dalle cifre binarie ottenute come resti, lette in ordine inverso. Confronta poi il 
risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero decimale in binario.
'''
decimale = int(input("Inserisci numero decimale: "))
resto = 0
binario = ""
binar = bin(decimale)
while decimale != 0:
    resto = str(decimale % 2)
    decimale = int(decimale / 2)
    binario = resto + binario
print ("Confronto dei risultati: ", binario,"e", binar)
