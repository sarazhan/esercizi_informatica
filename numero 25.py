'''
esercizio pagina 73 numero 25: a un concorso pubblico hanno partecipato due candidati di cui si sonoscono i nomi ei punteggo conseguiti.
Visualizza l'elenco dei due candidati prima in ordine alfabetico e in ordine descrescente di punteggio
'''
Nomea = input(" Nome: ")
Punteggioa = int(input("punteggio: "))
Nomeb = input(" Nome: ")
Punteggiob = int(input("punteggio: "))
Nomi = [Nomea,Nomeb]
Nomi.sort()
Punteggi = [Punteggioa, Punteggiob]
Punteggi.sort()
Punteggi.reverse()
print(" Nomi in modo alfabetico", Nomi, " Punteggi in modo decrescente", Punteggi)

