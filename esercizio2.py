'''
esercizio della scheda: scrivi un programma che data in entrata una lista A contenente n parole, 
restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
'''
listaA = input("Inserisci parole separate da uno spazio: ").split()
listaB =[]
for n in range (len(listaA)):
    parola = listaA[n]
    listaB.append(len(parola))
print("Ecco le loro lunghezze: ", listaB)