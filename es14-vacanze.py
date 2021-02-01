# esercizio numero 14 pag. 72: Analizza se il numero inserito sia pari o dispari.
a = int(input("Inserisci valore numerico a "))
b = int(input("Inserisci valore numerico b "))
prodotto = a*b
if prodotto <= 10:
    risultato = a+b
    print("addizione =", risultato)
    
else:
    risultato = a-b
    print("sottrazione =", risultato) 