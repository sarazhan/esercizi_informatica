'''
esercizio pagina 73 numero 27: i dati relativi al numero dei veicoli transitati in entrata a un casello autostradale sono inseriti giorno per giorno,
con una ripetizione che termina, quando si inserisce 0 come segnalazione della fine dell'input dei dati. Comunica il totaledei veicoli transitati nelperiodo considerato.
'''
somma = 0
conto = 0
while True:
    numero = int(input("scrivi numero veicoli per giorno: "))
    if numero == 0: 
        break
    else :
        somma += numero
        conto+= 1
print("Il totale dei veicoli per ", conto, "giorni è: %s" %somma)
