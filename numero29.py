'''
esercizio pag.73 numero 29: dato un elenco di città con l'indicazione per ciascuna di esse del nome della temperatura massima e minima registrate un giorno
si devono contare quante città hanno superato nel giorno un valore prefissato per l'escursione termica ottenuta per differenza tra temperatura massima e minima 
organizza un programma che dopo aver chiesto il valore da controllare dell'escursione termica per ogni città dell'elenco ripeta la richiesta dei dati nome 
temperatura massima e minima a calcoli l'escursione termica e controlli se l'escursione è maggiore del valore prefissato in questo caso incrementa il 
contatore delle città selezionate alla fine della ripetizione comunica il numero delle città registrato nel contatore
'''
lista_città = input("Scrivi la città poi stccato da uno spazio l'altra città: ").split()
conto = 0
temperatura_max = []
temperatura_min = []
differenze = []
for i in range(len(lista_città)):
    tmax = int(input("Quale la temperatura massima registrata in un giorno della città corrispondente? "))
    tmin = int(input("Quale la temperatura minima registrata in un giorno della città corrispondente? "))
    temperatura_max.append(tmax)
    temperatura_min.append(tmin)       
valore_fisso = int(input("Inserisce il valore fisso: "))
for n in range(len(temperatura_max)):
    differenza = temperatura_max[n] - temperatura_min[n]
    print("Le esursioni termiche sono: ", differenza)
    differenze.append(differenza)
for n in range(len(temperatura_max)):
    val = differenze[n]
    if val > valore_fisso:
        conto += 1
print("Questo è il conto: ",conto)
