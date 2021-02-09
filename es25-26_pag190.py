'''
Consgena 10/02/2021: 25. I voti assegnati a trenta studenti di una classe, una prova d'italiano sono memorizzati in un dizionario che ha per chiave la matricola, 
mentre il valore associato il voto elenca risultati in ordine crescente di voto e successivamente riducendo a uno i voti uguali. 
26. Con riferimento al dizionario dal problema precedente. elenca i studenti che hanno ottenuto una votazione superiore alla media di tutte le votazioni. 
'''
diz = {
"001" : 1, "002" : 7, "003" : 2, "004" : 2, "005" : 3, "006" : 3.5, "007" : 4, "008" : 5, "009" : 8, "010" : 5.5, "011" : 6,
"012" : 6.5, "013" : 7, "014" : 7.5, "015" : 8, "016" : 8.5, "017" : 9, "018" : 9.5, "019" : 10, "020" : 5, "021" : 3, "022" : 8,
"023" : 8, "024" : 6, "025" : 7, "026" : 8, "027" : 7, "028" : 10, "029" : 8, "030" : 6 }

voti = list(diz.values())
voti.sort()
print("Ecco i voti in ordine crescente:", voti)
diz_inverso = {voto : matricola for (matricola, voto) in diz.items()}
tipi_voti = len(diz_inverso)
print("Numero tipi di voti dati:", tipi_voti)

somma = sum(diz.values())
media = somma/30
studenti_suff = 0
for voto in voti:
    if voto > media:
        studenti_suff += 1
print("Il numero di alunni sufficienti è:", studenti_suff, "/ 30")
