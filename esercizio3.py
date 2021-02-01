'''
esercizio della scheda: un programma per il linguaggio "dei furfanti", raddoppiare ogni consonante di una parola e inserire una o in mezzo.
Dopo aver tradotto la parola " rovarspraket", attendere la traduzione di un'altra parola, se l'utente vuole.
 '''
vocali= [ "a", "e", "i" ,"o" , "u" ]
traduzioni = []
while True:
    parola = input("inserire parola da tradurre ")
    Testo = ""
    for lettera in parola:
        if lettera.lower() not in  vocali:
            Testo = Testo + lettera + "o" + lettera
        else:
            Testo = Testo + (lettera) 
    traduzioni.append(Testo)
    risposta = int(input("per inserire un'altra parola da tradurre inserire 1, per visualizzare la traduzione inserire 0: "))
    if risposta == 0:
        break
print(traduzioni)